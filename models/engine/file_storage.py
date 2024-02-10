#!/usr/bin/python3
"""Defines the FileStorage class."""
import os
import sys

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to the sys.path
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
grand_parent_dir = os.path.abspath(os.path.join(parent_dir, '..'))
sys.path.extend([parent_dir, grand_parent_dir])
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass

    def save(self):
        """Serializes the dictionary of objects to the JSON file.(after converting it to a dict)"""
        object_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(object_dict, f)
