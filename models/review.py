#!/usr/bin/env python3
"""
This module contains the Review class that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a review"""
    place_id = ''
    user_id = ''
    text = ''
