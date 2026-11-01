class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.start = None
        self.last = None

    def append(self, value):
        new_node = Node(value)
        if not self.start:
            self.start = new_node
            self.last = new_node
            return new_node
        self.last.next = new_node
        self.last = new_node
        return self.last

    def print_all_nodes(self):
        current = self.start
        if not current:
            print("Our list is empty")
            return
        while True:
            print("Current node is")
            print(current.__dict__)
            if not current.next:
                print("Found the last node")
                return
            current = current.next

my_list = SingleLinkedList()
my_list.append(45)
my_list.append(99)
my_list.append(134)
my_list.print_all_nodes()
