#!/usr/bin/python3
""" a class Square that defines a square """
class Square:
 """ defines a square """
 def __init__(self, size=0):
   """initialises a new square"""
   if not isinstance(size, int):
     raise TypeError("size must be an integer")
   elif size < 0:
     raise ValueError("size must be >= 0")
     """ Instantiation """
   self.__size = size
  
 
