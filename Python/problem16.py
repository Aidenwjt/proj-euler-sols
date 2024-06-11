#!/usr/bin/env python3

sum = 0
for digit in str(2**1000):
    sum += int(digit)

print('The answer is: {}'.format(sum))
