#!/usr/bin/python3
"""contains Square class to represent squares"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class to represent a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of a Square object
        Args:
            size (int): the size of the square
            x (int): the x coordinate
            y (int): the y coordinate
            id (int): the id of the object
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size attribute getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size attribute setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """formatted output"""
        s = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                              self.y, self.width)
        return s

    def update(self, *args, **kwargs):
        """updates a square with new values for attributes"""
        attrs = ["id", "width", "x", "y"]
        if args is not None and len(args) != 0:
            i = 0
            while i < len(attrs) and i < len(args):
                setattr(self, attrs[i], args[i])
                i += 1
        else:
            for attr in attrs:
                if attr == "width" and "size" in kwargs.keys():
                    setattr(self, attr, kwargs["size"])
                if attr in kwargs.keys():
                    setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """represents a Square as a dict"""
        rect_dict = {}
        attrs = ["id", "size", "x", "y"]
        for attr in attrs:
            if attr == "size":
                rect_dict.update({attr: getattr(self, "width")})
            else:
                rect_dict.update({attr: getattr(self, attr)})
        return rect_dict
