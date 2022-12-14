import requests
from sqlalchemy.orm import Session
from sqlalchemy import func
from db_main import People, Rooms, engine
from schedule import run_pending, every 
from faker import Faker
from random import randint, choice


def fill_rooms(amount_of_rooms):
    session = Session(engine)
    rooms = []
    for i in range(amount_of_rooms):
        room_num = randint(1, 500)
        floor = randint(1, 5)
        amount_of_bed = randint(1, 4)
        price = randint(1000, 10000)
        obj = Rooms(room_num=room_num, floor=floor, amount_of_bed=amount_of_bed, price=price)
        rooms.append(obj)
    print(*rooms, '---------------------------', sep='\n')
    session.add_all(rooms)
    try:
        session.commit()
    except:
        for room in rooms:
            print(room.room_num)
    return 'Success'


def fill_people():
    session = Session(engine)
    rooms = session.query(Rooms).all()
    people = []
    faker = Faker()
    names = [faker.name() for i in range(20)]

    print(len(rooms))
    for i in range(0, len(rooms), 2):
        print(f"I: {i}")
        room = rooms[i]
        print(room.room_num)
        name = choice(names)
        person_obj = People(names=name, room_num=room.room_num)
        people.append(person_obj)
    session.add_all(people)
    session.commit()


# def main():
#     every(1).minutes.do(fill_weather)
#     while True:
#         run_pending()

if __name__ == '__main__':
    fill_rooms(10)
    fill_people()