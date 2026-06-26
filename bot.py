import telebot
from database import add_user, get_balance

TOKEN = "8820192584:AAGEX2pUGI_qQV7Y5XTldwmJVlcyq0XwAMk"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    add_user(
        message.from_user.id,
        message.from_user.username
    )

    bot.reply_to(
        message,
        "✅ تم إنشاء حسابك بنجاح!\n\nأرسل أي رابط."
    )


@bot.message_handler(commands=['balance'])
def balance(message):
    bal = get_balance(message.from_user.id)
    bot.reply_to(message, f"💰 رصيدك الحالي: ${bal}")


@bot.message_handler(func=lambda message: True)
def check(message):
    text = message.text.strip()

    if text.startswith("http://") or text.startswith("https://"):
        bot.reply_to(message, f"✅ تم استلام الرابط:\n\n{text}")
    else:
        bot.reply_to(message, "❌ هذا ليس رابطًا صحيحًا.")


print("Bot is running...")

try:
    me = bot.get_me()
    print("Bot username:", me.username)
except Exception as e:
    print("ERROR:", e)

try:
    bot.infinity_polling(skip_pending=True)
except Exception as e:
    print("POLLING ERROR:", e)