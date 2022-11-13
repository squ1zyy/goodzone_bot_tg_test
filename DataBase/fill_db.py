import requests
from sqlalchemy.orm import Session
from db_main import People, Rooms, engine
from schedule import run_pending, every 
from faker import Faker
from random import randint


faker = Faker()
names = [faker.name() for i in range(40)]
print(names)


def fill_rooms():
    room_num = randint(1, 100)
    floor = randint(1, 5)
    amount_if_beds = randint(1, 4)
    


def fill_people():
    pass


# def main():
#     every(1).minutes.do(fill_weather)
#     while True:
#         run_pending()

if __name__ == '__main__':
    # fill_rooms()
    fill_people()