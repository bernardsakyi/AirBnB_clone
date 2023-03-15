#!/usr/bin/env python3
"""
This module contains the City class that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a city"""

    state_id = ''
    name = ''
