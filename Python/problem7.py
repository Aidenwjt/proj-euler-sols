#!/usr/bin/env python3

import numpy as np

# Consulting the Prime Number Theorem
N = 100000
no_primes = N/np.log(N)
while(no_primes <= 10001):
    N += 1
    no_primes = N/np.log(N)

"""
- The PNT tells us that our upper bound for N is 116684.
-  We will use the Miller-Rabin as our primality test, and since N < 1373653,
    then it is enough to just use a = 2 and a = 3 as witnesses.
"""
prime_counter = 2
for i in range(5,N,2):
    s = 0
    composite_flag = 0
    temp = i - 1
    while (temp % 2 == 0):
        s += 1
        temp = temp/2 
    d = int((i-1)/(pow(2,s)))
    for a in range(2,4):
        x = pow(a,d,i)
        y = 0
        for j in range(0,s):
            y = pow(x,2,i)
            if (y == 1 and x != 1 and x != i-1):
                composite_flag = 1
                break
            x = y
        if (composite_flag == 1):
            break
        if (y != 1):
            composite_flag = 1
            break
    if (composite_flag != 1):
        prime_counter += 1
    if (prime_counter == 10001):
        print("{}st: {}".format(prime_counter,i))
        break
