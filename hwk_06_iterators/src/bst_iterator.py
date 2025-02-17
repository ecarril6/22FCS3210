'''
CS3210 - Principles of Programming Languages - Fall 2022
Instructor: Thyago Mota
Description: Homework 06 - An iterator for a BST (Binary Search Tree)
Student Name: Emily Carrillo
'''

class BST: 

    # the labels for the nodes are obtained from a list of strings
    def __init__(self, labels): 
        if (not isinstance(labels, list)):
            raise Exception("labels must be a list!")
        if (not labels):
            raise Exception("labels must not be empty!")
        self.label = labels[0] # first label makes the root node 
        self.left = None
        self.right = None        
        for label in labels[1:]:
            BST._add(self, label)

    # adds a node with the given label to the BST using recursion
    def _add(node, label):
        if (label < node.label):
            if (node.left):
                BST._add(node.left, label)
            else:
                node.left = BST([label])
        else:
            if (node.right):
                BST._add(node.right, label)
            else:
                node.right = BST([label])

    # helper method that builds a string representation of the BST using recursion
    def _print(node, tabs = ""): 
        out = ""
        if (node):
            out += tabs + node.label + "\n"
            if node.left:
                out += BST._print(node.left, tabs + "   ")
            if node.right:
                out += BST._print(node.right, tabs + "   ")                
        return out

    def __str__(self):
        return BST._print(self, "")

    # helper method that builds a list with the elements of the BST in in-order order using recursion
    def _in_order(node): 
        nodes = []
        if (node):
            if (node.left):
                nodes += BST._in_order(node.left)
            nodes.append(node.label)
            if (node.right):
                nodes += BST._in_order(node.right)
        return nodes
    
    # TODOd #1: return an iterator for BST; hint: use _in_order to build a list with the (node) elements; then return "self"
    def __iter__(self):
        return iter(self._in_order())

    # TODOd #2: return the label of the first element from the list that you built in __iter__, updating the list before returning; hint: don't worry if the list is empty (the exception that is going to be thrown is used to notify that there are no more elements to return)
    def __next__(self) -> int:
        if self.label >= len(self._in_order):
            raise StopIteration
        else: 
            self.label += 1
            return self._in_order[self.label -  1]

# the code below builds and prints a tree using the given labels
tree = BST(["b", "a", "d", "c", "e"])
print("Tree:")
print(tree)

# TODOd #3: use the iterator that you created to show the labels of the elements of the tree
#create iteratot 
iterator = iter(tree)
try: 
    while True:
        print(next(iterator), " ", end = '')
except StopIteration:
    print("All traversed")

