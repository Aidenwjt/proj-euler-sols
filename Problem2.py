"""
Problem 2: Even Fibonacci Numbers
Description: Find the sum of the even number terms in the 
Fibonacci sequence whose values do not exceed four million.
"""

# This sequence starts with 1 and 2
base1 = 1
base2 = 2
# Get the 3rd term of the sequence
term = base1 + base2
# We know 2 is even so start with a sum equal to 2
sum = 2
while(term < 4000000):
    # If no remainder then it is even
    if term % 2 == 0:
        sum += term
    # Get the next term in the sequence
    base1 = base2
    base2 = term
    term = base1 + base2

print('The sum is: {}'.format(sum))