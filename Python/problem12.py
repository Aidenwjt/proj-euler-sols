#!/usr/bin/env python3

i = 3
i_prev = 1
while (True):
    # TODO: Need to use divisor counting function
    temp = i
    i = (i - i_prev) + 1
    i_prev = temp
