class Node:
    data: str
    next: 'Node'
    
    def __init__(self, data, next= None):
        self.data = data
        self.next = next
    
class DoubleEndedQueue:
    head: Node
    tail: Node
    
    def __init__(self, head):
        self.head = head
        self.tail = head
    
    def print_structure(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def push_right(self, new_node):
        current_node = self.head
        
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node
        self.tail = new_node
    
    def pop_left(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data
    
    def push_left(self, new_node):
        new_node.next = self.head
        self.head = new_node
    
    def pop_right(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            data = self.head.data
            self.head = self.tail = None
            return data
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            data = current_node.next.data
            current_node.next = None
            self.tail = current_node
            return data

#Load Structure
first_node = Node("Hola")
my_double_ended_queue = DoubleEndedQueue(first_node)

second_node = Node("Mundo")
my_double_ended_queue.push_right(second_node)

third_node = Node("soy")
my_double_ended_queue.push_left(third_node)

my_double_ended_queue.print_structure()
print("     ")

my_double_ended_queue.pop_left()
my_double_ended_queue.print_structure()

print("     ")

my_double_ended_queue.pop_right()
my_double_ended_queue.print_structure()

