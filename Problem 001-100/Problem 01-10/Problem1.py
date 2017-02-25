#!~/anaconda2/bin/python

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below N.
#
# Input Format
# 
# First line contains T that denotes the number of test cases. This is 
# followed by T lines, each containing an integer, N.
#
# Constraints
# 1 <= T <= 10^5
# 1 <= N <= 10^9
#
# Output Format
#
# For each test case, print an integer that denotes the sum of all the 
# multiples of 3 or 5 below N.

import sys
import math


def main():
    test_cases = int(raw_input().strip())
    
    for case in xrange(test_cases):
        N = int(raw_input().strip())
        
        sum_of_multiples = findSumOfMultiples(N, 3) + findSumOfMultiples(N, 5)
        sum_of_common_multiples = findSumOfCommonMultiples(N, 3, 5)
        print sum_of_multiples - sum_of_common_multiples


# Find the sum of the multiples using the "rainbow method" (that's what I
# learned it as, there might be another name). Basically sum the first and
# last multiple and multiply them by the number of pairs of numbers.
def findSumOfMultiples(N, x):
    N -= 1
    remainder = N % x
    final_multiple = N - remainder
    
    sum_of_pairs = final_multiple + x
    
    number_of_multiples = N / x

    # If there's an odd number of multiples we need to add the one in the
    # middle separately
    if(number_of_multiples % 2 == 0):
        return sum_of_pairs * (number_of_multiples / 2)
    else:
        sum_without_middle = sum_of_pairs * (number_of_multiples / 2)
        middle = ((number_of_multiples / 2) + 1) * x
        return sum_without_middle + middle


# Since using the findSumOfMultiples twice will add all of the common
# multiples twice, we need to find the sum of all them so we can subtract it
# from the total.
def findSumOfCommonMultiples(N, x, y):
    # Now we just do the same thing we did before but with the common multiple
    # instead of just x or y
    return findSumOfMultiples(N, x * y)


main()
