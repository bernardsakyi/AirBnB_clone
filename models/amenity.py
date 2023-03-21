#!/usr/bin/env python3
"""
This module contains the Amenity class that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class contains the name of an amenity"""
    name = ''
