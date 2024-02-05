#!/usr/bin/python3
'a class MyList that inherits from list'
class MyList(list):
 ' this class inherits from built-in type lists '
 def print_sorted(self):
  'prints sorted list'
  print(sorted(self))
