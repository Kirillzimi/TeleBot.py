import telebot
from bot_logic import gen_pass, flip_coin, get_duck_image_url

from telebot.async_telebot import AsyncTeleBot  
import asyncio
import random
import os
bot = telebot.TeleBot("7937749892:AAHwc2TQRhzO5mytinzbCDSV_Sbj2Rv2RVg")
async_bot = AsyncTeleBot("7937749892:AAHwc2TQRhzO5mytinzbCDSV_Sbj2Rv2RVg")    


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def get_password(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['coin'])
def get_coin(message):
    bot.reply_to(message, flip_coin())

@async_bot.chat_join_request_handler()
async def handle_chat_join_request(message: telebot.types.ChatJoinRequest):
    await async_bot.send_message(message.chat.id, "I accepted a new user!")
 
async def main():
    # Asynchronen Bot starten
    print("Asynchroner Bot wird gestartet...")
    asyncio.create_task(async_bot.polling())

    # Synchrone Bot-Logik in einem separaten Thread starten
    print("Synchroner Bot wird gestartet...")
    await asyncio.to_thread(bot.polling)


if __name__ == "__main__":
    asyncio.run(main())


@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir("memes"))
    with open(f'memes/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 
    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    try:
        image_url = get_duck_image_url()
        bot.reply_to(message, image_url)
    except Exception as e:
        bot.reply_to(message, "Не удалось получить изображение утки 😔")

print("BOT started")
bot.polling()
