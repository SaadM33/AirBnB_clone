#!/usr/bin/python3
"""the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


__classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF signal to exit the program"""
        print()  # print a new line for clarity
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
