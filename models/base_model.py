#!/usr/bin/python3
""" contains the base class"""

import os
import sys

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to the sys.path
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
grand_parent_dir = os.path.abspath(os.path.join(parent_dir, '..'))
sys.path.extend([parent_dir, grand_parent_dir])
import models
import uuid
from datetime import datetime

class BaseModel:
    """Represents the BaseModel of the HBnB project."""
     
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            models.storage.new(self)
    
     
    def save(self):
        """update updated_at variable with the current date"""
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """Returns a dictionary representation of self"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)