from json import dumps, loads

class Base:
    ''' Comment '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Comment'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        # Returns the JSON string representation of list_dictionaries
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        # Writes the JSON string representation of list_objs to a file
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as the_file:
            the_file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        # Returns the list of the JSON string representation json_string
        if json_string is not None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        # Returns an instance with all attributes already set
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        # Returns a list of instances
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as the_file:
            return [cls.create(**another_file) for another_file in cls.from_json_string(the_file.read())]

