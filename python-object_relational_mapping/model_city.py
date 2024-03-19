#!/usr/bin/python3
"""
This module contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    City class:
    - inherits from Base (imported from model_state)
    - links to the MySQL table cities
    - has id, name, and state_id attributes
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
