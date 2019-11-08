# Author: EL
# Date: 5 November 2019
# Description: Implement a binary search tree class

"""
Adapted from djra on Stack Overflow:
https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree
"""

class Tree:
    def __init__(self):
        self.root = self
        self.left = None
        self.right = None
        self.value = None

    def add(self, val):
        if(self.value == None):
            self.value = val
        else:
            self._add(val)

    def _add(self, val):
        if(val < self.value):
            if(self.left != None):
                self.left._add(val)
            else:
                self.left = Tree()
                self.left.value = val
        else:
            if(self.right != None):
                self.right._add(val)
            else:
                self.right = Tree()
                self.right.value = val

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val):
        if(val == self.value):
            return self.root
        elif(val < self.value and self.left != None):
            return self._find(val, self.left)
        elif(val > self.value and self.right != None):
            return self._find(val, self.right)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if(self.root != None):
            print(str(self.value))
        if (self.left != None):
            self._printTree(self.left)
        if (self.right != None):
            self._printTree(self.right)

    def _printTree(self, root):
        if(root != None):
            root.printTree()

"""
Test implementation
"""

test = Tree()
test.add(8)
test.add(13)
test.add(14)
test.add(3)
test.add(5)
test.printTree()