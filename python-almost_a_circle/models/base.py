#!/usr/bin/python3
"""Base class module - tests located in test/test_base.py"""
from json import dumps, loads
import csv
from os import path

class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list of dictionaries to a JSON string.
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string.
        Args:
            json_string (str): A string representing a list of dictionaries.
        Returns:
            list: The list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return loads(json_string)
    
        
    @staticmethod
    def from_json_string(json_string):
        """Deserialize a JSON string to a list of dictionaries.
        Args:
            json_string (str): A string representing a list of dictionaries.
        Returns:
            list: The list of dictionaries represented by json_string.
        """
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): A list of instances who inherits from Base.
        """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a JSON file."""
        filename = "{}.json".format(cls.__name__)
        if not path.isfile(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            new_obj = Rectangle(1, 1)
        elif cls == Square:
            new_obj = Square(1)
        else:
            new_obj = None
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a list of objects to a CSV file."""
        filename = '{}.csv'.format(cls.__name__)
        with open(filename, 'w', newline='', encoding="utf-8") as csvfile:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = "{}.json".format(cls.__name__)
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a list of objects from a CSV file."""
        filename = '{}.csv'.format(cls.__name__)
        if not path.isfile(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as csvfile:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            list_objs = []
            for row in reader:
                for key, value in row.items():
                    row[key] = int(value)
                list_objs.append(cls.create(**row))
            return list_objs
