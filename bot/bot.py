import datetime
from telegram.ext import Updater, CommandHandler


# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(update, context):
    print(update)
    print(context)
    botname = context.bot.username
    username = update.effective_chat.username
    fullname = update.effective_chat.first_name + ' ' + update.effective_chat.last_name
    missatge = "You are %s (%s) and I am %s." % (fullname, username, botname)
    context.bot.send_message(chat_id=update.effective_chat.id, text=missatge)


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='There ain\'t much I can help ya with.')


def time(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='It\'s ' + str(datetime.datetime.now()) + ', aka time for a break!')

    # declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('time', time))

# engega el bot
updater.start_polling()
