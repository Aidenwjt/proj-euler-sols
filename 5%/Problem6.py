"""
Problem 6: Sum square difference
Description: Find the difference between the sum of the squares
of the first one hundred natural nummbers and the square of the sum.
"""

# Variables to keep track of the sums
sum_of_squares = 0
sum = 0
# Loop through the first 100 natural numbers
for i in range(1,101):
    sum_of_squares += i**2
    sum += i
# Square the sum of the first 100 natural numbers
square_of_sum = sum**2
# Find the difference
difference = square_of_sum - sum_of_squares

print('The answer is: {}'.format(difference))