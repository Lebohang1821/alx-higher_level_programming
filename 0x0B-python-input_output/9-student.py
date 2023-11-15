#!/usr/bin/python3
"""It defines a class Student."""


class Student:
    """I represent student."""

    def __init__(self, first_name, last_name, age):
        """It initialize a new Student.

        Args:
            first_name (str): First name of student.
            last_name (str): Last name of student.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """It is a dictionary represent student."""
        return self.__dict__
