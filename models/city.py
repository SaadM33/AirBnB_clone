#!/usr/bin/python3
"""Defines the City class."""

import os
import sys

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to the sys.path
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
grand_parent_dir = os.path.abspath(os.path.join(parent_dir, '..'))
sys.path.extend([parent_dir, grand_parent_dir])
from models.base_model import BaseModel

class City(BaseModel):
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""