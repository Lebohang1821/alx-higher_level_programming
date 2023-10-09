#!/usr/bin/python3
"""Class MyInt that inherits from int."""


class MyInt(int):
    """It invert int operators == and !=."""

    def __eq__(self, value):
        """Change == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Change != operator to == behavior."""
        return self.real == value
