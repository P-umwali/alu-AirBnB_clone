import json
from msilib.schema import SelfReg
from typing import Self
import models

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
    try:
        from models import classes 
        with open(Self.__file_path, 'r') as file:
            obj_dict = json.load(file)
            for key, obj_dict in obj_dict.items():
                class_name, obj_id = key.split('.')
                # Obtain the class dynamically using the class name
                obj_class = getattr(models, class_name)
                obj_instance = obj_class(**obj_dict)
                Self.__objects[key] = obj_instance
    except FileNotFoundError:
        pass
