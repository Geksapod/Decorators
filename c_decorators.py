"""This module provide access to c-decorators"""

from typing import Callable
from typing import Any


class DecoratorReg:
    """
    This class used to decorate other classes.
    Decorated classes are registered in decorated_classes list.

    Attributes:
        decorated_classes: List of decorated classes.
    """

    decorated_classes = []

    def __init__(self, cls: Callable[[Any], object]):
        """
        Initialisation of DecoratorReg class.

        :param cls: Class to be decorated.
        """

        self.cls = cls

    def __call__(self, *args, **kwargs):
        """Call self as a function and add cls to decorated_classes list."""

        if self.cls not in self.decorated_classes:
            self.decorated_classes.append(self.cls)
        return self.cls(*args, **kwargs)


def add_str(string: str) -> str:
    """
    Return string + Callable[[object], str].

    :param string: String to be concatenated.
    """

    def decor_str(cls):

        def inner_str(*args, **kwargs):
            return f"{string}{str(cls(*args, **kwargs))}"

        return inner_str

    return decor_str


class Box:
    """
    This class used to represent a box.

    Attributes:
        x: Width of the box.
        y: Length of the box.
        z: Нeight of the box.
    """

    def __init__(self, x, y, z):
        """
        Initialisation of Box class.

        :param x: Width of the box.
        :param y: Length of the box.
        :param z: Нeight of the box.
        """
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        """Return volume of the box."""

        return self.x * self.y * self.z

    @staticmethod
    def total_volume(box_1, box_2):
        """Return total volume of two boxes."""

        return box_1.volume() + box_2.volume()

    def __str__(self):
        return f"{self.x}x{self.y}x{self.z}"
