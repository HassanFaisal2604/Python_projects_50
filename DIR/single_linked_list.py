class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert_val(self, value, location):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:
                newnode.next = self.head
                self.head = newnode
            elif location == -1:
                newnode.next = None  # Fixed: Set to None instead of Node
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1 and tempnode.next:  # Added check for tempnode.next
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
                if tempnode == self.tail:
                    self.tail = newnode

single_list = SinglyLinkedList()
single_list.insert_val(1, -1)  # Changed location to 0
single_list.insert_val(2, -1)  # Changed location to 0
single_list.insert_val(3, -1)  # Changed location to 0
print([node.data for node in single_list])  # Changed Node.value to node.data
