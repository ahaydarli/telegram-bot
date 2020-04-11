import re
from random import randrange

from flask import Flask, request
import telegram

bot_token = '1246937370:AAETkDNSx5-FZL4ty-2Ni7eUB-2_yAXUisw'
bot_user_name = '@oglanliq_bot'
URL = 'https://oglanlig-bot.herokuapp.com/'

global bot
global TOKEN
TOKEN = bot_token

bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    user_name = update.message.from_user.first_name

    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)
    try:
        if text in ['/start', '/oglan', '/oglan@oglanliq_bot']:
            bot_welcome = 'Oğlanlıq'
            bot.sendMessage(chat_id=chat_id, text=bot_welcome)
        elif text in ['/oglanlig', '/oglanlig@oglanliq_bot']:
            percent = randrange(1, 100, 1)
            bot_welcome = f'{user_name} - Oğlanlığın {percent}% 🌈'
            bot.sendMessage(chat_id=chat_id, text=bot_welcome)
    except Exception:
        bot.sendMessage(chat_id=chat_id, text="Oğlanlığında problem var !!!", reply_to_message_id=msg_id)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)
