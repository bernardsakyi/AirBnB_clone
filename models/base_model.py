#!/usr/bin/python3
"""base_model.py

This model contains a class BaseModel that defines all common attributes/methods for other classes:
"""
import uuid
from datetime import datetime
import models


class BaseModel():
	"""BaseModel
	
	This class defines all common methods and attributes for other classes
	"""
	
	def __init__(self, created_at, updated_at, id=None):
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
		
	
	def __str__(self):
		return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
	
	def save(self):
		"""save
		
		updates the public instance attribute updated_at with the current datetime
		"""
		self.update_at = datetime.now()
		
	def to_dict(self):
		"""to_dict
		
		returns a dictionary containing all keys/values of __dict__ of the instance of the basemodel:
		"""
		my_dict = self.__dict__.copy()
		my_dict['__class__'] = self.__class__.__name__
		my_dict['created_at'] = self.created_at.isoformat()
		my_dict['updated_at'] = self.updated_at.isoformat()
		return my_dict
