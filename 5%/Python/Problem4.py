#!/usr/bin/env python3

"""
TODO: 
This can definitely be optimized because I am checking duplicate pairs,
and also there is probably a more mathematical way of doing this.
"""
largest_palindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        s = str(product)
        # If the string is even length then just reverse the second
        # half and compare to the first half
        if len(s) % 2 == 0:
            s1 = s[:len(s)//2]
            s2 = s[len(s)//2:]
            s2_flipped = s2[::-1]
            if(s1 == s2_flipped):
                if(product > largest_palindrome):
                    largest_palindrome = product
        # If the string is odd length then reverse the second half,
        # remove the end character and compare to the first half
        else:
            s1 = s[:len(s)//2]
            s2 = s[len(s)//2:]
            s2_flipped = s2[::-1]
            s2_flipped_v2 = s2_flipped[:-1]
            if(s1 == s2_flipped_v2):
                if(product > largest_palindrome):
                    largest_palindrome = product

print('The answer is: {}'.format(largest_palindrome))


