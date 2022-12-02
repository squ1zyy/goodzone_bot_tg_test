from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Rooms(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    room_num = Column(Integer, nullable=False, unique=True)
    floor = Column(Integer)
    amount_of_bed = Column(Integer, nullable=False)
    person = relationship("People", back_populates='room')
    price = Column(Integer)


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    names = Column(String(40), nullable=False)
    room_num = Column(ForeignKey('rooms.room_num'))
    date = Column(DateTime(), default=datetime.now())
    room = relationship("Rooms", back_populates='person')


engine = create_engine('sqlite:///..//room.db')

if __name__ == "__main__":
    Base.metadata.create_all(engine)