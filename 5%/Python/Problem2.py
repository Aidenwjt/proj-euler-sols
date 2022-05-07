#!/usr/bin/env python3

base1 = 1
base2 = 2
term = base1 + base2
# We know 2 is even so start with a sum equal to 2
sum = 2
while(term < 4000000):
    if term % 2 == 0:
        sum += term
    base1 = base2
    base2 = term
    term = base1 + base2

print('The sum is: {}'.format(sum))
