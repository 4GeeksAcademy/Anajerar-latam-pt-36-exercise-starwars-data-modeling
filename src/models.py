import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    planet_name = Column(String(50), primary_key=True)
    population = Column(Integer)
    climate = Column(String(25))
    diameter = Column(Integer)
    gravity = Column(Integer)

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    name = Column(String(50), primary_key=True)
    birth_year = Column(String(15), nullable=False)
    gender = Column(String(10))
    height = Column(String(10))
    hair_color = Column(String(10))
    homeworld = Column(String(25),ForeignKey(Planets.planet_name))
    planet = relationship(Planets)

class Users(Base):
    __tablename__='users'
    user_id = Column(Integer,primary_key=True)
    user_name = Column(String(50), nullable=False)
    full_name = Column(String(100))
    email = Column(String(70))

class FavoritePlanets(Base):
    __tablename__='favorite_planets'
    id = Column(Integer, primary_key=True)
    planet_fav_name = Column(String(50),ForeignKey(Planets.planet_name))
    user_fav_id = Column(Integer,ForeignKey(Users.user_id))
    user = relationship(Users)
    planet = relationship(Planets)

class FavoritePeople(Base):
    __tablename__='favorite_people'
    id = Column(Integer,primary_key=True)
    people_fav_name = Column(String(50),ForeignKey(People.name))
    user_fav_id = Column(Integer,ForeignKey(Users.user_id))
    user = relationship(Users)
    people = relationship(People)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
