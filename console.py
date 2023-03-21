#!/usr/bin/python3
"""
Module that contains the entry point of the command interpreter
"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """This class contains method to operate the HBNB command console"""

    prompt = '(hbnb) '
    models_list = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                   "Review"]

    def emptyline(self):
        """Overwrite default to do nothing when empty line is entered"""
        pass

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program"""
        return True

    def do_create(self, arg):
        """Create a new instance of basemodel"""
        if (arg is None or len(arg) == 0):
            print('** class name missing **')
        elif (arg not in HBNBCommand.models_list):
            print('** class doesn\'t exist **')
        else:
            new_base = models.base_model.BaseModel()
            new_base.save()
            print(new_base.id)

    def do_show(self, line):
        """Print the string representation of an instance"""
        arg = line.split()
        if (line is None or len(line) == 0):
            print('** class name missing **')
        elif (arg[0] not in HBNBCommand.models_list):
            print('** class doesn\'t exist **')
        elif (len(arg) < 2):
            print('** instance id missing **')
        else:
            obj_dict = models.storage.all()
            key = f'{arg[0]}.{arg[1]}'
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        """Remove an instance by class name and id"""
        arg = line.split()
        if line is None or len(line) == 0:
            print('** class name missing **')
        elif arg[0] not in HBNBCommand.models_list:
            print('** class doesn\'t exist **')
        elif len(arg) < 2:
            print('** instance id missing **')
        else:
            obj_dict = models.storage.all()
            key = f'{arg[0]}.{arg[1]}'
            if key in obj_dict:
                del obj_dict[key]
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name"""

        obj_list = []
        obj_dict = models.storage.all()
        if arg is None or len(arg) == 0:
            for k, v in obj_dict.items():
                obj_list.append(str(v))
            print(obj_list)
        elif arg not in HBNBCommand.models_list:
            print('** class doesn\'t exist **')
        else:
            for k, v in obj_dict.items():
                if type(v).__name__ == arg:
                    obj_list.append(str(v))
            print(obj_list)

    def do_update(self, line):
        """Updates a instance based on class name and id"""
        arg = line.split()
        if line is None or len(arg) == 0:
            print('** class name missing **')
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
