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
    """
    Translating my C code from
    https://github.com/Aidenwjt/MATH-327-BYOA/blob/master/src/MRT/mrtest.c
    """
    
    # First need to find values s>0 and odd d>0 such that n-1 = 2^s * d
    temp = i - 1
    s = 0
    while(True):
        if(temp % 2 != 0):
            d = 1
            while(2**s * d != i-1):
                d += 2
            break
        temp /= 2
        s += 1

    # Now start the primality test with witness numbers a = 2 and a = 3
    composite_flag = 0
    break_flag = 0
    for a in range(2,4):
        x = pow(a,d,i)
        for k in range(0,s):
            y = pow(x,2,i)
            if((y==1) and (x!=1) and (x!= i-1)):
                break_flag = 1
                break
            x = y
        if(break_flag == 1):
            break
        if(y != 1):
            composite_flag = 1
            break
    if(composite_flag == 0):
        prime_counter += 1
        print("Prime number: {} - Prime counter: {}".format(i,prime_counter))
    if(prime_counter == 10001):
        print('The answer is: {}'.format(i))
        break
