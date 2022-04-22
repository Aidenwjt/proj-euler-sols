"""
Problem 3: Largest prime factor
Description: Find the largest prime factor of the
number 600851475143.
"""

## Checking if a number is prime
from sympy.ntheory import isprime

# Number in question
num = 600851475143

# Start with the smallest prime number
prime = 2

# Looping until num / prime = 1
while(num > 1):
    # Dividing the current num by the current 
    # prime until it does not divide exactly
    while(num % prime == 0):
        num = num / prime
    # If num is equal to prime then we have found our answer
    if num == 1:
        break
    # Find the next smallest prime
    prime += 1
    while(isprime(prime) != True):
        prime += 1

print('The largest prime factor is: {}'.format(prime))