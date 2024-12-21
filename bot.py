import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin 
  
bot = telebot.TeleBot("7937749892:AAHwc2TQRhzO5mytinzbCDSV_Sbj2Rv2RVg")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['random_password'])
def get_password(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = random_coin()
    bot.reply_to(message, {coin})





print("BOT started")
bot.polling()