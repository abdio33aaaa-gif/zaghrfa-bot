import telebot, os
from flask import Flask
import threading

TOKEN = os.getenv("TOKEN")
CHANNEL = "@BotKanal24"
CHANNEL_LINK = "https://t.me/BotKanal24"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
@app.route('/')
def home(): return "Bot is Live!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

def zagh(text):
    t = text.strip()
    styles = [
        f"꧁{t}꧂",
        f"★彡{t}彡★",
        f"༺{t}༻",
        f"『{t}』",
        f"◥{t}◤",
        f"〖{t}〗",
        f"꧁༒{t}༒꧂",
        f"🦋 {t} ",
        f"♛ {t} ♛",
        f"✨ {t} ✨",
        f"⚡ {t} ⚡",
        f"🔥 {t} 🔥",
        f"༄{t}༄",
        f"⫷{t}⫸",
        f"⋆ ˚｡{t}｡˚ ⋆",
        f"ꨄ {t} ꨄ",
        f"💞 {t} 💞",
        f"『⚜️{t}⚜️』",
        f"░{t}░",
        f"░▒▓█ {t} █▓▒░",
        f"𝒜 - {t}",
        f"𝕱𝖆𝖓𝖈𝖞 {t}",
        f"ⓕ {t} ⓕ",
    ]
    return "\n".join(styles)

def is_subscribed(user_id):
    try:
        member = bot.get_chat_member(CHANNEL, user_id)
        return member.status in ['member','administrator','creator']
    except Exception as e:
        print(e)
        return True

@bot.message_handler(commands=['start'])
def start(m):
    if not is_subscribed(m.from_user.id):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("اشترك بالقناة 🔔", url=CHANNEL_LINK))
        markup.add(telebot.types.InlineKeyboardButton("تأكيد الاشتراك ✅", callback_data="check_sub"))
        bot.send_message(m.chat.id, f"👋 هلا {m.from_user.first_name} ✨\n\n⚠️ مشان تستخدم بوت زغرفة الاسماء\nلازم تشترك بقناتنا الرسمية 👇\n\n{CHANNEL}\n\nبعد الاشتراك اكبس تأكيد الاشتراك", reply_markup=markup)
        return
    
    bot.send_message(m.chat.id, f"""هلا {m.from_user.first_name} ✨

أهلا فيك ببوت زخرفة الأسماء الاحترافي 😍

📌 القناة الرسمية: {CHANNEL}

🔹 ابعتلي أي اسم عربي أو انكليزي
🔹 رح زخرفلك ياه بـ 23 شكل فخم
🔹 كلها جاهزة للنسخ

يلا ابعت الاسم هلق 👇""")

@bot.callback_query_handler(func=lambda c: c.data=="check_sub")
def check(call):
    if is_subscribed(call.from_user.id):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "✅ تم تأكيد الاشتراك! نورّت\n\nابعتلي الاسم الي بدك زخرفتو هلق 👇")
    else:
        bot.answer_callback_query(call.id, "❌ لسا ما اشتركت بالقناة، اشترك اول!", show_alert=True)

@bot.message_handler(func=lambda x: True)
def handle(m):
    if not is_subscribed(m.from_user.id):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("اشترك بالقناة 🔔", url=CHANNEL_LINK))
        markup.add(telebot.types.InlineKeyboardButton("تأكيد الاشتراك ✅", callback_data="check_sub"))
        bot.send_message(m.chat.id, f"⚠️ لازم تشترك بالقناة اول {CHANNEL}", reply_markup=markup)
        return
    
    t=m.text
    if len(t) > 25:
        bot.send_message(m.chat.id, "الاسم طويل كتير 😅 ابعت اسم اقصر")
        return
        
    res = zagh(t)
    bot.send_message(m.chat.id, f"✨ زخرفة لـ: {t}\n\n{res}\n\n✅ ابعت اسم تاني")

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.infinity_polling()
