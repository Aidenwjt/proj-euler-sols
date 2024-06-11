#!/usr/bin/env python3

one_to_nine = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4

ten_to_nineteen = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8

twenty_to_ninetynine = (10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6)) + (8 * (one_to_nine))

onehundred_to_onethousand = (100 * 36) + (9 * 7) + (10 * 9 * 99) + ((one_to_nine + ten_to_nineteen + twenty_to_ninetynine) * 9) + 11

sum = one_to_nine + ten_to_nineteen + twenty_to_ninetynine + onehundred_to_onethousand

print('The answer is: {}'.format(sum))
