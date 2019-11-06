# Author: EL
# Date: 5 November 2019
# Description: Return a list of all the permutations of given array

"""
Write a recursive function that calculates all the permutations of a given array. For an
array of length n, there are n! different permutations. So for an array with three elements,
we will have 3 * 2 * 1 = 6 different permutations.
Example: permute_array([1, 2, 3]);
// => [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""

def permute_array(input_array):
    if len(input_array) <= 1: #if the array is empty or contains one character, the only permutation is itself
        return input_array
    elif len(input_array) == 2: #if the array has two characters, there are two permutations: itself and the reverse of itself
        return [input_array, input_array[::-1]]
    else:
    # if the array has three or more characters, the possible permutations are all the possible elements for the first item of the array,
    # with the permutations of all other items appended to that first element.
    # Procedurally, take each element of the input array and put it in front of all the permutations of the other elements
        return_array = []
        for index in range(0, len(input_array)):
            ele = input_array[index]
            subarrays = permute_array(input_array[0:index] + input_array[index + 1:])
            this_array = [[ele] + subarray for subarray in subarrays]
            return_array += this_array
        return return_array


