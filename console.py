#!/usr/bin/python3
"""console.py

This is a module that contains the entry point of the command
interpereter
"""

import cmd
from models.engine.file_storage import FileStorage
import json
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
import models




class HBNBCommand(cmd.Cmd):
	"""
	This class contains method to operate the HBNB command console
	"""
	model_list = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}
	prompt = '(hbnb)'
	
	def do_quit(self, arg):
		"""Quit command to exit the program"""
		return True
	
	def do_EOF(self, arg):
		"""Exits the program"""
		return True
	
	def do_create(self, arg):
		"""
		Creates a new instance of BaseModel, saves it (to 
		the JSON 
		file) and prints the id. Ex: $ create BaseModel
		"""
		if (arg is None or len(arg) == 0):
			print("** class name missing **")
		elif (arg not in HBNBCommand.model_list):
			print(" ** class doesn\'t exist ** ")
		else:
			new_base = models.base_model.BaseModel()
			new_base.save()
			print(new_base.id)
	
	def do_show(self, line):
		"""
		Prints the string representation of an 
		instance 
		based on  
		the class name and id
		Ex: $ show BaseModel 1234-1234-1234.
		"""
		arg = line.split()
		if (line is None or len(line) == 0):
			print("** class name missing **")
		elif (arg[0] not in HBNBCommand.model_list):
			print(" ** class doesn\'t exist ** ")
		elif (len(arg) < 2):
			print("** instance id missing **")
		else:
			obj_dict = models.storage.all()
			key = f'{arg[0]}.{arg[1]}'
			if key in obj_dict:
				print(obj_dict[key])
			else:
				print("** no instance found **")
				
	def do_destroy(self, line):
		"""
		Deletes an instance based on the class name 
		and id 
		(save the change into the JSON file). 
		Ex: $ destroy BaseModel 1234-1234-1234.
		"""
		arg = line.split()
		if (line is None or len(line) == 0):
			print("** class name missing **")
		elif (arg[0] not in HBNBCommand.model_list):
			print("** class doesn\'t exist **")
		elif (len(arg) < 2):
			print("** instance id missing **")
		else:
			obj_dict = models.storage.all()
			key = f'{arg[0]}.{arg[1]}'
			if key in obj_dict:
				del obj_dict[key]
				models.storage.save()
			else:
				print("** no instance found **")
	
	def do_all(self, arg):
		"""
		Prints all string representation of all
		instances based or not on the class name. 
		Ex: $ all BaseModel or $ all.
		"""
		
		obj_list = []
		obj_dict = models.storage.all()
		if arg is None or len(arg) == 0:
			for key, value in obj_dict.items():
				obj_list.append(str(value))
			print(obj_list)
		elif arg not in HBNBCommand.model_list:
			print("** class doesn\'t exist **")
		else:
			for key, value in obj_dict.items():
				obj_list.append(str(value))
			print(obj_list)
			
		
		
	def do_update(self, line):
		"""
		Updates an instance based on the class name and id by 
		adding or updating attribute (save the change into the 
		JSON file). Ex: $ update BaseModel 1234-1234-1234 
		email "aibnb@mail.com".
		"""
		arg = line.split()
		if line is None or len(arg) == 0:
			print('** class name missing**')
		elif arg[0] not in HBNBCommand.models_list:
			print('** class doesn\'t exist **')
		elif len(arg) < 2:
			print('** instance id missing **')
		else:
			obj_dict = models.storage.all()
			key = f'{arg[0]}.{arg[1]}'
			if key not in obj_dict:
				print('** no instance found **')
			elif len(arg) < 3:
				print('** attribute name missing **')
			elif len(arg) < 4:
				print('** value missing **')
			else:
				setattr(obj_dict[key], arg[2].strip('"'), arg[3].strip('"'))
					
if __name__ == '__main__':
	HBNBCommand().cmdloop()		
