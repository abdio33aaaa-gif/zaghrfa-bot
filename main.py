import telebot, os
from flask import Flask
import threading

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "هلا ✨ ابعتلي الاسم")

@bot.message_handler(func=lambda x: True)
def zag(m):
    t=m.text
    bot.send_message(m.chat.id, f"꧁{t}꧂\n★彡{t}彡★\n༺{t}༻\n『{t}』")

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.infinity_polling()
