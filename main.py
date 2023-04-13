import telebot
import random
from telebot import types
from core.config import TOKEN, IMAGE

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(content_types=['text'])
def send_user(message):
    # bot.send_message(message.chat.id, message.text)
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'hello {message.from_user.username}')
    elif message.text.lower() == 'image':
        bot.send_photo(message.chat.id, open(random.choice(IMAGE), 'rb'))
    else:
        bot.send_message(message.chat.id, f'Я не понимаю это: {message.text}')
    
    
bot.polling(non_stop=True)

