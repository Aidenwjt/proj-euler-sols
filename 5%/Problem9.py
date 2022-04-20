"""
Problem 9: Special Pythagorean triplet
Description: There exists exactly one Pythagorean triplet for which
a + b + c = 1000, find the product abc.
"""

from math import sqrt

# Looping through a thousand integers should be enough
for a in range( 0, 1001 ):
    for b in range( 0, 1001):
        # Calculate c using the pythagorean theorem
        c = sqrt( a**2 + b**2 )
        # Make sure we satisfy the constraints on a, b, and c
        if( a < b ) and (b < c):
            # Sum these values and check if it is equal to 1000
            if(a + b + c == 1000):
                # Print the answer with the values and just exit
                print("The answer is: {} (with a = {}, b = {}, and c = {})".format(int(a*b*c), a, b, int(c)))
                exit(0)