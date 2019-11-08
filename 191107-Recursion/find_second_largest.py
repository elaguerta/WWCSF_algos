# Author: EL
# Date: 07 November 2019
# Description: Find the second largest element of a binary tree

"""
Write a recursive function to find the 2nd largest element in a binary search tree.
"""



def second_largest(root):
    # if the root has a right child, then there are values greater than root
    if root.right is not None
        #if the root's right child has a right child, search that right grandchild
        if root.right.right is not None:
            return second_largest(root.right)
        #if the root's right child is a does not have a right child, then there are no values greater than this
        #child. Return the current value.
        else:
            return root.value

    # if there is no right child, but there is a left child, there are values less than root,
    # but no values greater than root. That means that root is the largest value, and its left child must be the
    # second largest value.
    elif root.left is not None:
        return root.left.value
    else:
    #if there is no right child, and no left child, then there is no second largest value.
        print("Tree with one node. There is no second largest value.")
        return root.value


