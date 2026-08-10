#math module

import math
print(math.pi)
print(math.pi*4)
print(math.sqrt(2))
print(math.log(2))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.pow(2,4))
print(math.ceil(4.9))
print(math.floor(3.11))

#from keyword
#by using from keyword we can import packages at a time

from math import pi,sqrt,log,tan,cos,sin,pow,ceil,floor
print(pi)
print(sqrt(4))
print(log(3))
print(tan(30))
print(cos(45))
print(sin(60))
print(pow(3,3))
print(ceil(8.11))
print(floor(6.51))

#sys module

import sys
print(sys.version)
print(sys.path)

#os module

import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.chdir("C:\\Users\\HP\\Downloads"))
print(os.listdir())
print(os.chdir("C:\\Users\\HP\\Downloads\\codegnan python"))
print(os.listdir())

#random module-random module is used to generate a random numbers in python,randint function is used and this function is define in random module

#random module-to print multiple random multiple integers

import random
a=random.sample(range(10,40),10)
print(a)

#randint()-to print a single random integer
#in randint the stop number can be given exactly it stops exactly at that number only

import random
a=random.randint(50,60)
print(a)

#choice()-to print a integer of our given input

import random
a=[30,40,50,60,70]
b=random.choice(a)
print(b)
