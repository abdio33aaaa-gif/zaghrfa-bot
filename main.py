import telebot, os
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "هلا ✨ ابعتلي الاسم")

@bot.message_handler(func=lambda x: True)
def zag(m):
    t=m.text
    bot.send_message(m.chat.id, f"꧁{t}꧂\n★彡{t}彡★\n༺{t}༻\n『{t}』")

bot.infinity_polling()
