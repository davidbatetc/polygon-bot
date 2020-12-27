import os
from cl.PolyParser import *
from cl.PolyLexer import *
from cl.PolyEval import *
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def handlesErrors(f):
    """
    A simple function decorator that runs the given function and produces
    an error message if the function raises an exception.

    Note: this decorator expects the first two arguments of the function
    to be the 'update' and 'context' arguments corresponding to the Telegram
    message handlers.
    """
    def handler(*args):
        try:
            f(*args)
        except Exception as e:
            try:
                update, context = args[0], args[1]  # Defined for better readibility
                print('Error of type \'{:}\' detected: \'{:}\''.format(type(e).__name__, str(e)))
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='An error was detected. Please try again.'
                )
            except Exception as _:
                print('It was not possible to inform the user about the error.')
    return handler


@handlesErrors
def start(update, context):
    """
    Function that gets executed when /start is called. Sends a message to the
     user in which the bot is presented.
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Hi {:}, @{:} here! I\'m a bot that replies with text messages and images to operations '
        'related to convex polygons. If this is your first time texting me, you might '
        'want to use /help to see what I can do for you.'.format(
            update.effective_chat.first_name, context.bot.username)
    )


@handlesErrors
def help(update, context):
    """
    Function that gets executed when /help is called. Sends a message to the
     user with the instructions on how the Telegram bot works.
    """
    if len(context.args) > 1 or (len(context.args) == 1 and context.args[0] != 'program'):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='The /help command expects either "/help" or "/help program". No '
            'other arguments are accepted. Try again!'
        )
    elif len(context.args) == 0:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='I\'ll be happy to help you out! You can use the following commands:\n'
            '- Use /start to receive a short presentation about me.\n'
            '- Use /help to receive an explanation of how I work.\n'
            '- Use /begin to start a new program. If you don\'t know what a program '
            'is, just keep reading and you will find out soon!\n'
            '- Use /end to finish a program.\n'
            '- Use /sample n to see the source code of the sample program number n '
            'and the output resulting from its execution. This can be a good way to '
            'see what I can do for you.\n'
            '- Use /clear to delete the images that you have created from the '
            'computer that is hosting me.\n\n'
            'Need more information? Type "/help program" in order to see the commands '
            'that you can use in your program.'
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Let me tell you about programs. A new program begins when you send me '
            'a message with /begin, as long as there is no other program running. In order '
            'to finish a running program, you just have to send me a message with /end. '
            'All the messages sent between the message with /begin and the message with /end '
            'are assumed to be part of the program, and are immediately executed, producing '
            'the corresponding output. Find below the commands that you can use in the program.\n\n'
            '*Generating polygons*\n'
            'There are several ways to generate a convex polygon in the program:\n'
            '- `[x0 y0  x1 y1  x2 y2  ...]` returns convex polygon obtained by computing '
            'the convex hull of the given list of points.\n'
            '- `#p` returns the bounding box of the polygon `p`.\n'
            '- `p*q` returns the intersection between the polygons `p` and `q`.\n'
            '- `p + q` returns the convex union between the polygons `p` and `q`, which is '
            'defined as the convex hull of the vertices of `p` and `q`.\n'
            '- `copy p` returns a copy of the polygon stored in the variable `p`. Note that '
            'in this case `p` has to be a variable.\n'
            '- `regular n, r, cx cy, angle` returns a regular polygon of radius `r` with '
            '`n` vertices and centered on the point (`cx`, `cy`). `angle` is the angle of rotation '
            'of the polygon, in radians. If the `angle` is zero, then the right-most vertex '
            'of the polygon lies on the line {y = `c.y`}.\n'
            '- `!n` returns a convex polygon obtained by computing the convex hull of a set '
            'of `n` randomly generated points.\n\n'
            '*Commands*\n'
            'In each line of the program, either a command or an empty line is expected. '
            'Comments, which are explained below, are ignored. The commands that can be '
            'used are the following:\n'
            '- `q := p` assigns the polygon `p` to the variable `q`. Note that if `p` is '
            'a variable, then `q` and `p` will be the same, meaning that any changes '
            'applied to `p` will affect `q` as well, and viceversa.\n'
            '- `color p, {r g b}` sets the color of the polygon `p` to the color given '
            'by the red, green and blue values `r`, `g` and `b` of the RGB color space. '
            'For each value, a floating point number between `0` and `1` is expected.\n'
            '- `print p` prints the vertices of the polygon `p` in a new line.\n'
            '- `print "text"` prints a `text` in a new line.\n'
            '- `area p` prints the area of the polygon `p` in a new line.\n'
            '- `perimeter p` prints the perimeter of the polygon `p` in a new line.\n'
            '- `vert p` prints the number of vertices of the polygon `p` in a new line.\n'
            '- `centroid p` prints the centroid of the polygon `p` in a new line.\n'
            '- `inside p, q` prints `yes` if the polygon `p` is inside the polygon `q`, '
            'and prints `no` otherwise.\n'
            '- `equal p, q` prints `yes` if the polygon `p` is equal to the polygon `q`, '
            'and prints `no` otherwise.\n'
            '- `draw "image.png", p1, p2, p3, ...` creates a 400x400 image with the '
            'polygons `p1`, `p2`, `p3`, ...\n'
            '- `translate p, vx vy` translates the polygon `p` by the vector `v = (vx, vy)`. '
            'Note that in this case `p` has to be a variable.\n'
            '- `rotate p, alpha` rotates `p` an angle `alpha` around its centroid. '
            'Note that in this case `p` has to be a variable.\n'
            '- `scale p, k` scales the polygon `p` with respect to its centroid by a '
            'factor `k`.\n\n'
            '*Comments*\n'
            'Your programs can also include comments. Comments are preceded by `//`. '
            'Whenever a `//` is found, the following characters are ignored until the '
            'end of the line.\n\n'
            '*Final recommendation*\n'
            'The amount of information in this message might be a bit overwhelming in '
            'the beginning. For this reason, it is recommended to first run a few '
            'sample programs in order to see these commands in practice. In order to '
            'do so, just run "/sample n", with n being the number of the sample program, '
            'for example, "/sample 2". That\'s all, enjoy!',
            parse_mode=telegram.ParseMode.MARKDOWN
        )


@handlesErrors
def begin(update, context):
    """
    Function that gets executed when /begin is called. Begins a new program unless
     there is a program already running. In that case it sends an error message.

    This function sets context.chat_data['isProgramRunning'] to True. Furthermore,
     it creates a new visitor, which gets stored in context.chat_data['visitor'].
    """
    if 'isProgramRunning' in context.chat_data and context.chat_data['isProgramRunning']:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='There is already an ongoing program. Finish that program with /end '
            'before beginning a new program.'
        )
    else:
        context.chat_data['isProgramRunning'] = True
        context.chat_data['visitor'] = PolyEval()
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You have begun a new program. Text me your program and send a message '
            'with /end when you are done. Please note that all the messages that you send '
            'before the message with /end will be interpreted as being part of the program! '
            'If you are a bit lost, you can use /help.'
        )


@handlesErrors
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
            text='There is no program running! Use /begin to start a new program.'
        )


@handlesErrors
def showSample(update, context):
    """
    Function that gets executed when /sample is called. It sends the source code
    of a sample program and also the output of its execution.

    The /sample command takes one parameter, the number of the sample program,
    and when called with '/sample n' it will look for the sample program in the
    file 'sample-program-n.poly' and produce the corresponding output if it is
    possible to access it.
    """
    if len(context.args) != 1:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='A single argument is expected for the /sample command. For example, '
            'you can use "/sample 2" in order to run the sample program number 2. '
            'Type /help for more information.'
        )
        return

    if 'isProgramRunning' in context.chat_data and context.chat_data['isProgramRunning']:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='There is already an ongoing program. Finish that program with /end '
            'before beginning a new program.'
        )
        return

    fileName = 'sample-program-{:}.poly'.format(context.args[0])
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            programText = file.read()

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Running program "{:}". Program source code:'.format(fileName)
        )
        if programText:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='`' + programText + '`',
                parse_mode=telegram.ParseMode.MARKDOWN
            )

            lexer = PolyLexer(InputStream(programText))
            parser = PolyParser(CommonTokenStream(lexer))
            tree = parser.root()
            outputText, imageNames = PolyEval().visit(tree)

        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Empty file, nothing to be shown.'
            )
            outputText, imageNames = '', []

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Program output:'
        )

        if outputText:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='`' + outputText + '`',
                parse_mode=telegram.ParseMode.MARKDOWN
            )

        if 'imageNames' not in context.chat_data:
            context.chat_data['imageNames'] = set()

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
            text='I attempted to run "{:}", but I encountered an error. Try running '
            'another sample program.'.format(fileName)
        )


@handlesErrors
def handleProgramContent(update, context):
    """
    Function that gets called whenever the user sends a text message.

    This function expects lines of a program. If a program is running, then the
     lines are executed as a part of that program and the resulting output is sent
     as a message, including images. If no program is running, a message suggesting
     the user to begin a new program is sent.
    """
    print(
        'User {:} {:} (@{:}) sent:'.format(
            update.effective_chat.first_name,
            update.effective_chat.last_name,
            update.effective_chat.username),
        update.message.text
    )

    if 'isProgramRunning' not in context.chat_data:
        context.chat_data['isProgramRunning'] = False

    if context.chat_data['isProgramRunning']:
        lexer = PolyLexer(InputStream(update.message.text))
        parser = PolyParser(CommonTokenStream(lexer))
        tree = parser.root()
        outputText, imageNames = context.chat_data['visitor'].visit(tree)

        if outputText:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='`' + outputText + '`',
                parse_mode=telegram.ParseMode.MARKDOWN
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
            text='There is currently no program running. You might want to begin a '
            'new program using /begin. Type /help for more information.'
        )


@handlesErrors
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
            text = text + 'The following images have been deleted: "' + \
                '", "'.join(successfulImageSet) + '"\n'
        if failedImageSet:
            text = text + 'It was not possible to delete: "' + \
                '", "'.join(failedImageSet) + '"\n'

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
dispatcher.add_handler(CommandHandler(command='start', callback=start))
dispatcher.add_handler(CommandHandler(command='help', callback=help))
dispatcher.add_handler(CommandHandler(command='begin', callback=begin))
dispatcher.add_handler(CommandHandler(command='end', callback=end))
dispatcher.add_handler(CommandHandler(command='sample', callback=showSample))
dispatcher.add_handler(CommandHandler(command='clear', callback=clear))
dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=handleProgramContent))

# Turns on the bot
updater.start_polling()
updater.idle()
