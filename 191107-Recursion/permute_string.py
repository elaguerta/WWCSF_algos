# Author: EL
# Date: 5 November 2019
# Description: Return all permutations of a string as a set

"""
Write a recursive function for generating all permutations of an input string. Return them
as a set.
"""

def permute_string(input_str):
    if len(input_str) <= 1: #if the string is empty or contains one character, the only permutation is itself
        return set([input_str])
    elif len(input_str) == 2: #if the string has two characters, there are two permutations: itself and the reverse of itself
        return set([input_str, input_str[::-1]])
    else:
    # if the string has three or more characters, the set of all the permutations is the union
    # of all the possibilities for the first character, with the permutations of all other characters appended to that first character.
    # Procedurally, take each character and put it in front of all the permutations of the rest of the characters
        return_set = set()
        for index in range(0, len(input_str)):
            char = input_str[index]
            substrings = permute_string(input_str[0:index] + input_str[index + 1:])
            this_set = {char + substring for substring in substrings}
            return_set = return_set.union(this_set)
        return return_set


