from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DataBase.db_main import People, Rooms
from Config.config import TOKEN
from requests import get
from telebot import TeleBot, types


engine = create_engine('sqlite:///rooms.db')
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, f"❗ Привет, {msg.from_user.first_name}\n\n❗ Спасибо что используешь нашего бота!\n❗Вот список функций которые в нем есть: /start /help /get_room /people_info")
    bot.send_photo(msg.chat.id, get("https://planetofhotels.com/sites/default/files/atttaction-images/71765171.jpg").content)

print('ПРОСТО В СОЛО, УБЬЮ ВСЕХ БЛ***, ААААААААААААААААААА')
bot.polling(none_stop = True)