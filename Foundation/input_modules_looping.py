import math
import datetime
import random
import re

#input


my_name = input("Enter your name: ")
print(my_name)

my_age = int(input("How old are you? "))

my_age =  my_age+ 5
print(my_age)





#inbuilt functions
'''
 e.g. input or print
not part of a module - already pre-packed in python
don't have to build it or install it etc
'''



#import additional (external) modules
'''
they're already in python just need to be activated in the project
they each take space in memory which is why they're not automatically added
google to check what's available e.g. : math module python and see W3School or docs.Python.org for more info
imports must be at the very top!!!!!

examples:
 import datetime - DO NOT USE THIS FOR THE ASSIGNMENT
 import math - EASY
 import random - EASY
 import copy - DIFFICULT
 import timeit - AVOID
 import re - DO NOT TRY USING THIS

from math import_pi - this will import pi from math module only so it doesn't import the whole module/library
then print(pi) instead of print(math.pi)
'''
print(math.pi)
print(datetime.date.today())



