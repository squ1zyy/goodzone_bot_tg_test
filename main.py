from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DataBase.db_main import People, Rooms
from Config.config import TOKEN
from requests import get
from telebot import TeleBot, types


engine = create_engine('sqlite:///room.db')
bot = TeleBot(TOKEN)


def get_query(cls):
    session=Session(engine)
    rooms_query = session.query(cls)
    session.close()
    return rooms_query


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, f"❗ Привет, {msg.from_user.first_name}\n\n❗ Спасибо что используешь нашего бота!\n❗Вот список функций которые в нем есть: /start /help /get_room")
    bot.send_photo(msg.chat.id, get("https://planetofhotels.com/sites/default/files/atttaction-images/71765171.jpg").content)


@bot.message_handler(commands=['list_rooms'])
def list_rooms(msg):
    query = get_query(Rooms)
    rooms = query.all()
    i = 0
    for room in rooms:
        i += 1
        bot.send_message(msg.chat.id, f'Room {i}: {room.room_num}')


@bot.message_handler(commands=['get_room'])
def get_persons_in_room(msg):
    bot.send_message(msg.chat.id, text="Enter room num: ")
    bot.register_next_step_handler(msg, get_person)


def get_person(msg):
    room_num = msg.text
    query = get_query(Rooms)
    room = query.filter(Rooms.room_num == room_num).first()
    if not room:
        bot.send_message(msg.chat.id, f"Room №{room_num} doesn't exist")
        return None
    if not room.person:
        bot.send_message(msg.chat.id, "Room is free")
    for person in room.person:
        bot.send_message(msg.chat.id, f'Full name: {person.names}')
    bot.send_message(msg.chat.id, f'Amount of beds in room №{room_num}: {room.amount_of_bed}\n Price of room №{room_num}: {room.price}')


@bot.message_handler(commands=['add_booking'])
def add_booking(msg):
    bot.send_message(msg.chat.id, "How many persons will live in room: ")
    bot.register_next_step_handler(msg, get_name)

def get_name(msg):
    query = get_query(Rooms)
    available_rooms = query.filter(Rooms.amount_of_bed == msg.text, Rooms.person == None).all()
    if not available_rooms:
        bot.send_message(msg.chat.id, "Available room from your request doesn't found")
        return None
    for room in available_rooms:
        bot.send_message(msg.chat.id, room.room_num)
        bot.send_message(msg.chat.id, f'Names: {room.person}')


print('!!!')
bot.polling(none_stop = True)