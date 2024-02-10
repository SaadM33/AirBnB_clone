#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary of serialized objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the dictionary of serialized objects."""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing
        """
        class_map = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as text_file:
                obj_dict = json.load(text_file)

                for key, val in obj_dict.items():
                    class_name = val['__class__']
                    class_instance = class_map[class_name]
                    instance = class_instance(**val)
                    all_objects = self.all()
                    all_objects[key] = instance
        except FileNotFoundError:
            pass

    def save(self):
        """Serializes the dict of objs to JSON file after converting to dict"""
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)
