import os
from cl.PolyParser import *
from cl.PolyLexer import *
from cl.PolyEval import *
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def help(update, context):
    """
    Function that gets executed when /help is called. Sends a message to the
     user with the instructions on how the Telegram bot works.
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='There ain\'t much I can help ya with.')


def start(update, context):
    """
    Function that gets executed when /start is called. Begins a new program unless
     there is a program already running. In that case it sends an error message.

    This function sets context.chat_data['isProgramRunning'] to True. Furthermore,
     it creates a new visitor, which gets stored in context.chat_data['visitor'].
    """
    if 'isProgramRunning' in context.chat_data and context.chat_data['isProgramRunning']:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='There is already an ongoing program. Finish that program with /end '
            'before starting a new program.'
        )
    else:
        context.chat_data['isProgramRunning'] = True
        context.chat_data['visitor'] = PolyEval()
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have started a new program. Text me your program and send a message '
            'with /end when you are done. Please note that all the messages that you send '
            'before the message with /end will be interpreted as being part of the program! '
            'If you are a bit lost, you can use /help.'
        )


def end(update, context):
    """
    Function that gets executed when /end is called. Ends the running program
     unless there is no program running. In that case it sends an error message.

    This function sets context.chat_data['isProgramRunning'] to False.
    """
    if 'isProgramRunning' not in context.chat_data:
        context.chat_data['isProgramRunning'] = False

    if context.chat_data['isProgramRunning']:
        context.chat_data['isProgramRunning'] = False
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Program finished, have a fantastic day!'
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='There is no program running! Use /start to begin a new program.'
        )


def showSample(update, context):
    """
    Function that gets executed when /sample is called. It sends the source code
    of a sample program and also the output of its execution.

    The /sample command takes one parameter, the number of the sample program,
    and when called with '/sample n' it will look for the sample program in the
    file 'sample-program-n.txt' and produce the corresponding output if it is
    possible to access it.
    """
    if len(context.args) != 1:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Only one argument is expected for the /sample command. For example, '
            'you can use \"/sample 2\" in order to run the sample program number 2. '
            'Type /help for more information.'
        )
        return

    if 'isProgramRunning' in context.chat_data and context.chat_data['isProgramRunning']:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='There is already an ongoing program. Finish that program with /end '
            'before starting a new program.'
        )
        return

    fileName = 'sample-program-{:}.txt'.format(context.args[0])
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            programText = file.read()

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Running program \"{:}\". Program source code:'.format(fileName)
        )
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=programText
        )

        lexer = PolyLexer(InputStream(programText))
        parser = PolyParser(CommonTokenStream(lexer))
        tree = parser.root()
        outputText, imageNames = PolyEval().visit(tree)

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Program output:'
        )

        if 'imageNames' not in context.chat_data:
            context.chat_data['imageNames'] = set()

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=outputText
        )
        for imageName in imageNames:
            context.chat_data['imageNames'].add(imageName)
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=open(imageName, 'rb')
            )
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Program finished.'
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='I attempted to run \"{:}\", but I encountered an error. Try running '
            'another sample program.'.format(fileName)
        )


def handleProgramContent(update, context):
    """
    Function that gets called whenever the user sends a text message.

    This function expects lines of a program. If a program is running, then the
     lines are executed as a part of that program and the resulting output is sent
     as a message, including images. If no program is running, a message suggesting
     the user to start the program is sent.
    """
    if 'isProgramRunning' not in context.chat_data:
        context.chat_data['isProgramRunning'] = False

    if context.chat_data['isProgramRunning']:
        lexer = PolyLexer(InputStream(update.message.text))
        parser = PolyParser(CommonTokenStream(lexer))
        tree = parser.root()
        text, imageNames = context.chat_data['visitor'].visit(tree)

        if text:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=text
            )
        if 'imageNames' not in context.chat_data:
            context.chat_data['imageNames'] = set()

        for imageName in imageNames:
            context.chat_data['imageNames'].add(imageName)
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=open(imageName, 'rb')
            )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='There is currently no program running. You might want to start a '
            'new program using /start. Type /help for more information.'
        )


def clear(update, context):
    """
    Function that gets executed when /clear is called. Deletes the images that
     have been generated by the program from the bot hoster.
    """
    if 'imageNames' not in context.chat_data:
        context.chat_data['imageNames'] = set()

    imageSet = context.chat_data['imageNames']
    if imageSet:
        successfulImageSet = []
        failedImageSet = []
        for imageName in imageSet:
            if os.path.exists(imageName):
                os.remove(imageName)
                successfulImageSet.append(imageName)
            else:
                failedImageSet.append(imageName)

        text = ''
        if successfulImageSet:
            text = text + 'The following images have been deleted: \"' + \
                '\", \"'.join(successfulImageSet) + "\"\n"
        if failedImageSet:
            text = text + 'It was not possible to delete: \"' + \
                '\", \"'.join(failedImageSet) + "\"\n"

        context.chat_data['imageNames'] = set(failedImageSet)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='There are no images to be deleted.'
        )


# Creates objects to work with Telegram
TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add commands to the bot
dispatcher.add_handler(CommandHandler(command='help', callback=help))
dispatcher.add_handler(CommandHandler(command='start', callback=start))
dispatcher.add_handler(CommandHandler(command='end', callback=end))
dispatcher.add_handler(CommandHandler(command='sample', callback=showSample))
dispatcher.add_handler(CommandHandler(command='clear', callback=clear))
dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=handleProgramContent))

# Turns on the bot
updater.start_polling()
updater.idle()
