class Node:
    data: str
    left: 'Node'
    right: 'Node'

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left   
        self.right = right

class BinaryTree:
    root: Node

    def __init__(self, root):
        self.root = root

    def print_structure(self):
        current_node = self.root
        self._print_structure(current_node)

    def _print_structure(self, current_node):
        if current_node is not None:
            print(current_node.data)
            self._print_structure(current_node.left)
            self._print_structure(current_node.right)

#Load Structure
first_node = Node("Papa y Mama")
my_tree = BinaryTree(first_node)

second_node = Node("Hijo 1")
first_node.left = second_node
third_node = Node("Hijo 2")
first_node.right = third_node

my_tree.print_structure()