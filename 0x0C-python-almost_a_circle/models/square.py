#!/usr/bin/python3
"""
Module documentation goes here.
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method to initialize Square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes using both no-keyword and keyword arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

if __name__ == "__main__":
    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)

