from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from cl.PolyEval import *
from cl.PolyLexer import *
from cl.PolyParser import *


# Defines a function that gets executed when /help is called
def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='There ain\'t much I can help ya with.')


# Defines a function that gets executed when /start is called
def start(update, context):
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
            'before the message with /end will be interpreted as being part of the program!'
        )


# Defines a function that gets executed when /end is called
def end(update, context):
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


# For user messages handling
def handleMessage(update, context):
    if 'isProgramRunning' not in context.chat_data:
        context.chat_data['isProgramRunning'] = False

    if context.chat_data['isProgramRunning']:
        lexer = PolyLexer(InputStream(update.message.text))
        parser = PolyParser(CommonTokenStream(lexer))
        tree = parser.root()
        text, images = context.chat_data['visitor'].visit(tree)

        if text:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=text
            )
        for image in images:
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=open(image, 'rb')
            )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='There is currently no program running. You might want to start a '
            'new program using /start. Type /help for more information.'
        )


# Creates objects to work with Telegram
TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add commands to the bot
dispatcher.add_handler(CommandHandler(command='help', callback=help))
dispatcher.add_handler(CommandHandler(command='start', callback=start))
dispatcher.add_handler(CommandHandler(command='end', callback=end))
dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=handleMessage))

# Turns on the bot
updater.start_polling()
updater.idle()
