#!/usr/bin/python3
"""
Class Student that defines a student
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes Student instance with first name, last name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """Replace all attributes of Student instance with values from json"""
        for key, value in json.items():
            setattr(self, key, value)
