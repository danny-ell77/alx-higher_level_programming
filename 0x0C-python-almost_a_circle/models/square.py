#!/usr/bin/python3
"""This is the Square module.
Contains the Square class that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle and defines a Square object."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the default attributes of the Base object.
        Args:
            size (int): the size of a square side.
            x (int): the wanted horizontal (x) padding of the square.
            y (int): the wanted vertical (y) padding of the square.
            id (int): the wanted identifier of the Base object.
        """
        super(Square, self).__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """Overrides the default behaviour of the __str__ method."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get and Set the size attribute of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"size": self.size, "x": self.x, "y": self.y, "id": self.id}

    def update(self, *args, **kwargs):
        """Updates the Square attributes.
        Args:
            args (list): attributes to be modified [id, size, x, y].
            kwargs (dict): attributes to be modified.
        """
        if args is not None and len(args) > 0:
            props = ["id", "size", "x", "y"]
            for prop, value in zip(props, args):
                setattr(self, prop, value)
        else:
            for key, value in kwargs.items():
                if key == "id" and value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                if hasattr(self, key):
                    setattr(self, key, value)
