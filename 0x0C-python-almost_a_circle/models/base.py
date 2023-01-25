#!/usr/bin/python3
"""This is the Base module.
Contains the Base class which will be the
“base” of all other classes in this project.
"""
import json
import csv


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal is to manage id attribute in all our future classes
    and to avoid duplicating the same code and same errors.
    Attributes:
        __nb_objects (int): the number of created Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the default attributes of the Base object.
        Args:
            id (int): the identifier of the Base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): a list of objects.
        """
        if json_string is not None and len(json_string) >= 1:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

        # return cls(**dictionary)

    @classmethod
    def save_to_file(cls, list_objs):
        """Returns the list of the JSON string representation json_string.
        Args:
            json_string (str): string representing a list of dictionaries.
        """
        content = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                content.append(obj.to_dictionary())

        with open(f"{cls.__name__}.json", "w") as f:
            f.write(json.dumps(content))

    @classmethod
    def load_from_file(cls):
        """Returns an instance with all attributes already set.
        Args:
            dictionary (dict): the values of the wanted instance.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as f:
                items = cls.from_json_string(f.read())
                return [cls.create(**item) for item in items]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes the CSV string representation of list_objs to a file.
        Args:
            list_objs (list): a list of objects.
        """
        fields = []
        with open(cls.__name__ + ".csv", "w") as f:
            if list_objs is None or len(list_objs) <= 0:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes the CSV string representation
        of list_objs from a file.
        """
        fields = []
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=fields)
                dcts = [dict([k, int(v)] for k, v in line.items()) for line in reader]
                return [cls.create(**dct) for dct in dcts]

        except IOError:
            return []
