from json import dumps, loads
import csv

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        # serializes in CSV
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                        for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                        for obj in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='', encoding="utf-8") as my_file:
            written = csv.writer(my_file)
            written.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        # deserializes in CSV
        from models.rectangle import Rectangle
        from models.square import Square
        listing = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='', encoding="utf-8") as my_file:
                reader = csv.reader(my_file)
                for row in reader:
                    row = [int(des) for des in row]
                    if cls is Rectangle:
                        rect = {"id": row[0], "width": row[1], "height": row[2], "x": row[3], "y": row[4]}
                    else:
                        rect = {"id": row[0], "size": row[1], "x": row[2], "y": row[3]}
                    listing.append(cls.create(**rect))
        return listing

    @staticmethod
    def draw(list_rectangles, list_squares):
        from time import sleep
        from random import randrange
        import turtle
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            s = turtle.Turtle()
            s.color((randrange(255), randrange(255), randrange(255)))
            s.pensize(1)
            s.penup()
            s.pendown()
            s.setpos((i.x + s.pos()[0], i.y - t.pos()[1]))
            s.pensize(10)
            s.forward(i.width)
            s.left(90)
            s.forward(i.height)
            s.left(90)
            s.forward(i.width)
            s.left(90)
            s.forward(i.height)
            s.left(90)
            s.end_fill()

        sleep(5)
