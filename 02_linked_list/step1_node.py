# Array [] -> Object -> Linked List -> Tree, Graph etc.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_node(self):
        current = self
        print("Current value", current.value)
        print("Has next", current.next)
        if current.next:
            print(current.next.__dict__)

# Manual way of adding nodes (build from the end)
c = Node(value=18, next=None)
b = Node(value=35, next=c)
a = Node(value=20, next=b)

print("Node A is"); a.print_node()
print("Node B is"); b.print_node()
print("Node C is"); c.print_node()
