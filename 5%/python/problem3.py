#!/usr/bin/env python3

from sympy.ntheory import isprime

num = 600851475143

prime = 2

while(num > 1):
    while(num % prime == 0):
        num = num / prime
    if num == 1:
        break
    # Find the next smallest prime
    prime += 1
    while(isprime(prime) != True):
        prime += 1

print('The largest prime factor is: {}'.format(prime))
