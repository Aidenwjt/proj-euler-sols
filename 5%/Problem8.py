"""
Problem 8: Largest product in a series
Description: Find the thirteen adjacent digits in the 1000-digit
number that have the greatest product, and find the product.
"""

# Represent the number as a string so we can slice it
number= "73167176531330624919225119674426574742355349194934"\
        "96983520312774506326239578318016984801869478851843"\
        "85861560789112949495459501737958331952853208805511"\
        "12540698747158523863050715693290963295227443043557"\
        "66896648950445244523161731856403098711121722383113"\
        "62229893423380308135336276614282806444486645238749"\
        "30358907296290491560440772390713810515859307960866"\
        "70172427121883998797908792274921901699720888093776"\
        "65727333001053367881220235421809751254540594752243"\
        "52584907711670556013604839586446706324415722155397"\
        "53697817977846174064955149290862569321978468622482"\
        "83972241375657056057490261407972968652414535100474"\
        "82166370484403199890008895243450658541227588666881"\
        "16427171479924442928230863465674813919123162824586"\
        "17866458359124566529476545682848912883142607690042"\
        "24219022671055626321111109370544217506941658960408"\
        "07198403850962455444362981230987879927244284909188"\
        "84580156166097919133875499200524063689912560717606"\
        "05886116467109405077541002256983155200055935729725"\
        "71636269561882670428252483600823257530420752963450"

# We now want to know how many products of thirteen adjacent digits
# of this number we can have
choices = len(number) - 13

# Now lets begin slicing all the possible choices
# i will be our first digit and j will be our last digit
# greatest product will keep track of our answer
i = 0
greatest_product = 0
greatest_digits = ""
for j in range( 13, choices ):
    # Get the current 13 digits
    digits = number[i:j]
    # Initalize the product to be the value of the first digit
    product = ord( digits[0] ) % 48
    # If the value of the first digit is 0 then the whole product is 0
    if ( product == 0 ):
        # Increment the starting index
        i+=1
        continue
    # Loop through the rest of the digits and get the product
    for k in range( 1, len(digits) ):
        product *= ( ord(digits[k]) % 48 )
        # If the product is ever 0 then just break out
        if ( product == 0 ):
            break
        # If we have reached the end of iterations and the product is
        # greater than our greatest so far, replace it
        if ( k == len(digits) - 1 ) and ( product > greatest_product ):
            greatest_product = product
            greatest_digits = digits
    # Increment the starting index
    i += 1

# Print out our answer
print("The answer is: {} (with digits {})".format(greatest_product,greatest_digits))
