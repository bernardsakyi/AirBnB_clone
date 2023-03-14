#!/usr/bin/python3
"""console.py

This is a module that contains the entry point of the command
interpereter
"""

import cmd, sys
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models

class HBNBCommand(cmd.Cmd):
	"""
	This class contains method to operate the HBNB command console
	"""
	model_list = {'BaseModel': BaseModel}
	prompt = '(hbnb)'
	
	def do_quit(self, arg):
		"""Quit command to exit the program"""
		return True
	
	def do_EOF(self, arg):
		"""Exits the program"""
		return True
	
	def do_create(self, arg):
		"""
		Creates a new instance of BaseModel, saves it (to the JSON 
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
	
	def do_show(self, arg):
		"""
		Prints the string representation of an instance based on  
		the class name and id
		"""
		if (arg is None or len(arg) == 0):
			print("** class name missing **")
		elif (arg not in HBNBCommand.model_list):
			print(" ** class doesn\'t exist ** ")
		else:
			pass
	
	
	
	
	
			
		
if __name__ == '__main__':
	HBNBCommand().cmdloop()	
	
