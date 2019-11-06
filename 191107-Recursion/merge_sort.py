# Author: EL
# Date: 5 November 2019
# Description: Sort using recursion

"""
Given an unsorted array implement mergeSort and a helper function, merge, to sort the
array. Example: mergeSort([2, 5, 1, 3, 7, 2, 3, 8, 6, 3]); // => [1, 2, 2, 3, 3, 3, 5, 6, 7, 8]
"""

def mergeSort(array):
    num_elements = len(array)

    # If the array has zero or one elements, it's already sorted, so return it
    if num_elements <= 1:
        return array

    # otherwise, divide the array in half. Sort each half and merge the results.
    else:
        midpoint = num_elements // 2
        left = array[0:midpoint]
        right = array[midpoint:]
        return merge(mergeSort(left), mergeSort(right))

def merge(left_array, right_array):
    """
    :param left_array: A sorted array
    :param right_array: A sorted array
    :return: The merged, sorted array containing elements of both arrays
    """
    return_array = []

    # Destructively iterate through each element of the input arrays.
    # Each iteration of the while loop compares the first elements of each array.
    # We store the lesser of the two first elements in the return_array, then delete the element from the original
    # input array, shifting the input array's elements leftwards.

    while len(left_array) != 0 and len(right_array)!= 0:
        if left_array[0] <= right_array[0]:
            return_array += [left_array[0]]
            left_array = left_array[1:]
        else:
            return_array += [right_array[0]]
            right_array = right_array[1:]

    # when we break out of the while loop, we will have exhausted one of the two arrays.
    # If elements remain in the other array, append them to return_array
    if len(left_array) > 0:
        return_array += left_array
    elif len(right_array) > 0:
        return_array += right_array

    return return_array









