#!/usr/bin/env python3

# TODO: My god, the runtime... (split up the numbers and use multi-threading? Good way to learn how to use threads in python)

biggest_chain_size = 1
starting_number = 1
for i in range(2,1000000):
    n = i
    chain_size = 1
    while(n > 1):
        if(n % 2 == 0):
            n = n / 2
        else:
            n = 3*n + 1
        chain_size += 1
    if(chain_size > biggest_chain_size):
        biggest_chain_size = chain_size
        starting_number = i

print('The answer is: {}'.format(starting_number))
