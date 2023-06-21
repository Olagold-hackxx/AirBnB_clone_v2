#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey

class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = Column(String(60), ForeignKey(states.id))
    name = Column(String(128), nullable=False)
