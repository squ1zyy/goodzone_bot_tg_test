from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DataBase.db_main import People, Rooms
from Config.config import TOKEN
from requests import get
from telebot import TeleBot, types


engine = create_engine('sqlite:///room.db')
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, f"❗ Привет, {msg.from_user.first_name}\n\n❗ Спасибо что используешь нашего бота!\n❗Вот список функций которые в нем есть: /start /help /get_room")
    bot.send_photo(msg.chat.id, get("https://planetofhotels.com/sites/default/files/atttaction-images/71765171.jpg").content)


@bot.message_handler(commands=['get_room'])
def get_persons_in_room(msg):
    room_num = int(msg.text.split()[1])
    session = Session(engine)
    room = session.query(Rooms).filter(Rooms.room_num == room_num).first()
    if not room:
        bot.send_message(msg.chat.id, f"Room №{room_num} doesn't exist")
        return None
    if not room.person:
        bot.send_message(msg.chat.id, "Room is free")
    for person in room.person:
        first_name = person.names.split()[0]
        last_name = person.names.split()[1]
        bot.send_message(msg.chat.id, f'First name: {first_name} \nLast name: {last_name}')
        bot.send_message(msg.chat.id, f'Amount of beds in room №{room_num}: {room.amount_of_bed}')
        bot.register_next_step_handler(msg, msgg )
        bot.send_message(msg.chat.id, f'Price of room №{room_num}: 1000$')

    session.close()
def msgg(msg, room_num):
    pass


print('!!!')
bot.polling(none_stop = True)