import telebot, os
from flask import Flask
import threading

TOKEN = os.getenv("TOKEN")
CHANNEL = "@BotKanal24"
CHANNEL_LINK = "https://t.me/BotKanal24"

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is Live - @BotKanal24"

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
        f"🦋 {t} 🦋",
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
        f"░▒▓█ {t} █▓▒░",
        f"𝑭𝒂𝒏𝒄𝒚 {t}",
        f"𝕱𝖗𝖆𝖐𝖙𝖚𝖗 {t}",
        f"Ⓕ {t} Ⓕ",
        f"𝒜𝓁𝒷𝒶𝓈𝒽𝒶 -> {t}",
    ]
    return "\n".join(styles)

def is_subscribed(user_id):
    try:
        member = bot.get_chat_member(CHANNEL, user_id)
        return member.status in ['creator', 'administrator', 'member']
    except Exception as e:
        print(f"CHECK ERROR: {e}")
        return False

@bot.message_handler(commands=['start'])
def start(m):
    if not is_subscribed(m.from_user.id):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("🔔 اشترك بالقناة", url=CHANNEL_LINK))
        markup.add(telebot.types.InlineKeyboardButton("✅ تأكيد الاشتراك", callback_data="check_sub"))
        bot.send_message(m.chat.id, f"👋 هلا {m.from_user.first_name}!\n\n⚠️ مشان تستخدم بوت الزخرفة\nلازم تشترك بقناتنا الرسمية 👇\n\n{CHANNEL}\n\nبعد ما تشترك اكبس تأكيد الاشتراك", reply_markup=markup)
        return
    
    bot.send_message(m.chat.id, f"هلا {m.from_user.first_name} ✨\n\nانا بوت زخرفة الاسماء الاحترافي 😍\n\n📌 قناتنا: {CHANNEL}\n\n🔹 ابعتلي اي اسم عربي او انكليزي\n🔹 رح زخرفلك ياه بـ 23 شكل فخم\n\nيلا ابعت الاسم هلق 👇")

@bot.callback_query_handler(func=lambda c: c.data=="check_sub")
def check(call):
    if is_subscribed(call.from_user.id):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "✅ تم تأكيد الاشتراك! منور\n\nابعتلي الاسم الي بدك زخرفتو هلق 👇")
    else:
        bot.answer_callback_query(call.id, "❌ لسا ما اشتركت بالقناة! اشترك اول وبعدين اكبس تأكيد", show_alert=True)

@bot.message_handler(func=lambda x: True)
def handle(m):
    if not is_subscribed(m.from_user.id):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("🔔 اشترك بالقناة", url=CHANNEL_LINK))
        markup.add(telebot.types.InlineKeyboardButton("✅ تأكيد الاشتراك", callback_data="check_sub"))
        bot.send_message(m.chat.id, f"⚠️ يا {m.from_user.first_name} لازم تشترك {CHANNEL} اول", reply_markup=markup)
        return
    
    if len(m.text) > 25:
        bot.send_message(m.chat.id, "الاسم طويل كتير 😅 ابعت اسم اقصر من 25 حرف")
        return
        
    res = zagh(m.text)
    bot.send_message(m.chat.id, f"✨ زخرفة لـ: {m.text}\n\n{res}\n\n✅ ابعت اسم تاني")

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    print("Bot Started...")
    bot.infinity_polling()
