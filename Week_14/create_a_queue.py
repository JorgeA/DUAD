class Node:
    data: str
    next: 'Node'

    def __init__(self, data, next= None):
        self.data = data
        self.next = next

class Queue:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def enqueue(self, new_node):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data

#Load Structure
first_node = Node("Hola")
my_queue = Queue(first_node)

second_node = Node("Mundo")
my_queue.enqueue(second_node)

third_node = Node("third")
my_queue.enqueue(third_node)

forth = Node("forth")
my_queue.enqueue(forth)

my_queue.print_structure()

#Testing Methods
print(" ")
print("FIRST DEQUEUE")

my_queue.dequeue()
my_queue.print_structure()

print(" ")
print("SECOND DEQUEUE")

my_queue.dequeue()
my_queue.print_structure()
