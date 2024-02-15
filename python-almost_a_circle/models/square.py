#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        
        Args:
            size (int): The size of the square sides.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.width

    @size.setter
#    def size(self, value):
#        self.width = self.height = value

    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

#    def update(self, *args, **kwargs):
#        """Update the Square attributes."""
#        attrs = ['id', 'size', 'x', 'y']
#        if args and len(args) > 0:
#            for attr, value in zip(attrs, args):
#                if hasattr(self, attr):
#                    setattr(self, attr, value)
#        else:
#            for key, value in kwargs.items():
#                if hasattr(self, key):
#                    setattr(self, key, value)

     def update(self, *args, **kwargs):
        """Update the Square attributes."""
        if args and len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for attr, arg in zip(attrs, args):
                if hasattr(self, attr):
                    setattr(self, attr, arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    # Special handling for 'size' to ensure it sets both width and height
                    if key == 'size':
                        self.size = value
                    else:
                        setattr(self, key, value)
                    
    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.size}
