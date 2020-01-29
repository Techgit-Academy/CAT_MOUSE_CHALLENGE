#!/bin/python
 
import math
 
def catAAndCatB(x, y, z):
     x,y,z = [int(x),int(y),int(z)]
     catA = abs(x-z)
     catB = abs(y-z)
     if (catA < catB):
        print(catA)
     elif (catB < catA):
        print(catB)
     else:
        print('catC')
catAAndCatB(2, 5, 4)