#!/usr/bin/env python3

"""
TODO:
Probably a better starting value and increment value to reduce the runtime.
"""

i = 40
while(True):
    for j in range(1,21):
        if(i % j != 0):
            break
        if(j == 20):
            print('The answer is: {}'.format(i))
            exit(0)
    i += 20
