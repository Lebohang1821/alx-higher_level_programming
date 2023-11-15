#!/usr/bin/python3

"""It efines base model class."""
import json
import csv
import turtle


class Base:
    """My Base model.

    It represents "base" for all other classes*.

    Private Class Attributes:
        __nb_object (int): Num instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """It initialize Base.

        Args:
            id (int): Identity of Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """It returns JSON serialization of list of dicts.

        Args:
            list_dictionaries (list):List of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """It write JSON serialization of list of objects - file.

        Args:
            list_objs (list): List of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """It eturn deserialization of JSON string.

        Args:
            json_string (str): JSON str represent list of dicts.
        Returns:
            If json_string is None / empty to empty list.
            Otherwise - List represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """It return class instantied from dictionary of attributes.

        Args:
            **(dict): A Key/value pairs attributes - initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                _new = cls(1, 1)
            else:
                _new = cls(1)
            _new.update(**dictionary)
            return _new

    @classmethod
    def load_from_file(cls):
        """It return list classes instantiated from file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If file does not exist to empty list.
            Oe else - list on instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """It writes CSV serialization of list of objects - file.

        Args:
            list_objs (list): My list on inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """It return list of classes instantiated from CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If file does not exist to empty list.
            Otherwise - list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """It draw Rectangles and Squares using turtle module.

        Args:
            list_rectangles (list): Rectangle objects - draw.
            list_squares (list): Square objects - draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
