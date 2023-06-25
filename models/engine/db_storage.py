#!/usr/bin/python3
"""This is the database storage class for AirBnB"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

all_classes = {'State': State, 'City': City,
               'User': User, 'Place': Place,
               'Review': Review, 'Amenity': Amenity}


class DBStorage:
    __engine = None
    __session = None

    classes = [State, City]
    __user = getenv("HBNB_MYSQL_USER")
    __passwd = getenv("HBNB_MYSQL_PWD")
    __host = getenv("HBNB_MYSQL_HOST")
    __db = getenv("HBNB_MYSQL_DB")

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(self.__user, self.__passwd,
                                              self.__host, self.__db),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query and return all objects or specify class"""
        obj_dict = {}
        if cls:
            for row in self.__session.query(cls).all():
                # populate dict with objects from storage
                obj_dict.update({'{}.{}'.
                                format(type(cls).__name__, row.id,): row})
        else:
            for key, val in all_classes.items():
                for row in self.__session.query(val):
                    obj_dict.update({'{}.{}'.
                                    format(type(row).__name__, row.id,): row})
        return obj_dict

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute """
        self.__session.close()
