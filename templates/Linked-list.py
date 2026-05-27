class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next: # current.next for appending at end
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current: # i need to visit/print/reverse all the nodes
            if current.next:
                print(current.data,end="->")
            else:
                print(current.data) 
            current = current.next

# Example usage
if __name__ == "__main__":  
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    linked_list.print_list()