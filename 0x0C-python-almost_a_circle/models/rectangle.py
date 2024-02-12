#!/usr/bin/python3
"""
Module documentation goes here.
"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle class inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method to initialize Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.
        """
        self.validate_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.
        """
        self.validate_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Getter method for x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x attribute.
        """
        self.validate_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y attribute.
        """
        self.validate_non_negative_integer("y", value)
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Print the rectangle using '#' characters.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Update attributes using both no-keyword and keyword arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of the Rectangle instance.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def validate_positive_integer(self, name, value):
        """
        Validate if the value is a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("{} must be a positive integer".format(name))

    def validate_non_negative_integer(self, name, value):
        """
        Validate if the value is a non-negative integer.
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError("{} must be a non-negative integer".format(name))

if __name__ == "__main__":
    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)

