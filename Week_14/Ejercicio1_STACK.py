class Node:
    data: str
    next: 'Node'

    def __init__(self, data, next= None):
        self.data = data
        self.next = next

class Stack:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data

#Load Structure
first_node = Node("Hola")
my_stack = Stack(first_node)
#my_stack.print_structure()

second_node = Node("Mundo")
my_stack.push(second_node)
#my_stack.print_structure()

third_node = Node("soy")
my_stack.push(third_node)
my_stack.print_structure()
print("     ")
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.print_structure()