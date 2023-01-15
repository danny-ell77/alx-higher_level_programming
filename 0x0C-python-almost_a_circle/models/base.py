import json
import csv

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
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
        content = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                content.append(obj.to_dictionary())

        with open(f'{cls.__name__}.json', 'w') as f:
            f.write(json.dumps(content))

    @classmethod
    def load_from_file(cls):
        filename = f'{cls.__name__}.json'
        try:
            with open(filename, 'r') as f:
                items = cls.from_json_string(f.read())
                return [cls.create(**item) for item in items]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ...

    @classmethod
    def load_from_file_csv(cls):
        ...
