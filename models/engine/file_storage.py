#!/usr/bin/python3
"""This module defines the file storage class for AirBnB"""
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages serialization of instances to a JSON file and deserialization of a JSON file to instances.
    Attributes:
        __file_path: path to the JSON file.
        __objects: objects will be stored.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of objects.
        Return:
            Returns a dictionary of __objects.
        """
        result_dict = {}
        if cls:
            for key in self.__objects:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if partition[0] == cls.__name__:
                    result_dict[key] = self.__objects[key]
            return result_dict
        else:
            return self.__objects

    def new(self, obj):
        """Sets __objects to the given obj.
        Args:
            obj: given object.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes the file path to JSON file path."""
        serializable_dict = {}
        for key, value in self.__objects.items():
            serializable_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(serializable_dict, f)

    def reload(self):
        """Deserializes the file path to JSON file path."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in json.load(f).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an existing element."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """Calls reload()."""
        self.reload()
