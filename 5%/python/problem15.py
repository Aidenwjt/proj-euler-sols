#!/usr/bin/env python3

# It seems like this involves some cringe combinatorics (@NoahPinel probably freaked out when he realized this)
# https://stemhash.com/counting-lattice-paths/ (basic idea)

from sympy import factorial

# '40 choose 20'
k = 20
n = 40
paths = factorial(n) / ( factorial(n - k) * factorial(k) )

print('The answer is: {}'.format(paths))
