#!/usr/bin/python3
"""Defines a class Student."""

class Student:
    """Represents a student with basic information."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student object.

        Args:
            attrs (list, optional): A list of attribute names to include in the dictionary.
                If provided, only these attributes will be included.

        Returns:
            dict: A dictionary representation of the Student object.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json_data):
        """Replace all attributes of the Student object with values from a dictionary.

        Args:
            json_data (dict): A dictionary containing key-value pairs to update the attributes.
        """
        for key, value in json_data.items():
            setattr(self, key, value)
