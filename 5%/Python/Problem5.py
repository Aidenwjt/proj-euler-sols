"""
Problem 5: Smallest multiple
Description: Find the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20.
"""

# TODO: Probably a better starting value and increment value to reduce the runtime

# Start with 40 as this is the next multiple of 20 after 20
i = 40
# While true loop as we will kill the program in the loop
while(True):
    # Loop through 1 to 20
    for j in range(1,21):
        # Cut if one of the numbers do not evenly divide the current number
        if(i % j != 0):
            break
        # If all values evenly divide the current number then we have found an answer
        if(j == 20):
            print('The answer is: {}'.format(i))
            exit(0)
    # Increment by the largest divisor
    i += 20