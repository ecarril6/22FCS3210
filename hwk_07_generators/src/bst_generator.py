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

    # TODO #1: return one element at a time from the BST's given node and respecting in-order tree traversal
    # hint: do it recursively; the base-case is when node is None
    def in_order(node): 
        elements= []
        if node.left: # visit left tereee first
            elements += node.left.in_order()

        elements.append(node.label) # visit base element

        if node.right: # visit right nodes
            elements += node.right.in_order()


        return elements

# the code below builds and prints a tree using the given labels
tree = BST(["b", "a", "d", "c", "e"])
print("Tree:")
print(tree)


# TODO #2: use the generator that you created to show the labels of the elements of the tree
print(tree.in_order())
