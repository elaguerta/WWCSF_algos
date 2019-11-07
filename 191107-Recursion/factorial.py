# Author: EL
# Date: 07 November 2019
# Description: Compute the factorial using recursion
"""
Find the factorial of a given number N using recursion. (Beginner)
Ex: 	Input: 5 Output: 120
Explanation:  Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to N such as 5! = 120 (i.e. 5 * 4 * 3 * 2 * 1)
"""

def factorial(n):
    """
    :param n: An integer greater than or equal to 0.
    :return: n!
    """
    if n == 0:
        return 1 #by definition, 0! = 1
    else:
        return n * factorial(n-1)