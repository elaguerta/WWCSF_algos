# Author: EL
# Date: 5 November 2019
# Description: Calculate nth Fibonacci number, use memoization

"""
Write a recursive function that takes an integer n and returns the nth Fibonacci number.
To avoid a repeat of additional function calls implement memoization.
Example: fibonacci(0); // => 0 fibonacci(1); // => 1 fibonacci(2);
"""
fib_hash = {}

def fib(n):
    """
    :param n: The index of a term in the fibonacci sequence, with fib(0) = 0, fib(1) = 1, fib(2) = 1
    :return: The nth fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n in fib_hash.keys():
        return fib_hash[n]
    else:
        answer = fib(n - 1) + fib(n - 2)
        fib_hash[n]  = answer
        return answer



