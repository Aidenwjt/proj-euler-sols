#!/usr/bin/env python3

sum = 0
for i in range(0,1000):
    if( (i % 3 == 0) or (i % 5 == 0) ):
        sum += i
print('The sum is: {}'.format(sum))
