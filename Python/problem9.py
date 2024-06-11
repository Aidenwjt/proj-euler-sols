#!/usr/bin/env python3

from math import sqrt

for a in range( 0, 1001 ):
    for b in range( 0, 1001):
        c = sqrt( a**2 + b**2 )
        if( a < b ) and (b < c):
            if(a + b + c == 1000):
                print("The answer is: {} (with a = {}, b = {}, and c = {})".format(int(a*b*c), a, b, int(c)))
                exit(0)
