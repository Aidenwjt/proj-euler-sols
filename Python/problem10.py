#!/usr/bin/env python3

import numpy as np
from math import floor

prime_sum = 10
witnesses = [2,3,5]
# Is it required to start a the next prime after the largest witness prime?
for i in range(7,2000000,2):
    s = 0
    composite_flag = 0
    temp = i - 1
    while (temp % 2 == 0):
        s += 1
        temp = temp/2 
    d = int((i-1)/(pow(2,s)))
    #for a in range(2,min(i-2,floor(2*((np.log(i))**2)))):
    for a in witnesses:
        print(a)
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
        prime_sum += i
print("{}".format(prime_sum))
