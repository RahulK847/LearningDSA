class Node:
    """Represents a node in a doubly linked list."""

    def __init__(self, data):
        """Initializes a new node with data."""
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Represents a doubly linked list."""

    def __init__(self):
        """Initializes an empty list."""
        self.head = None

    def is_empty(self):
        """Checks if list is empty."""
        return self.head is None

    def display(self):
        """Prints data of all nodes."""
        current = self.head
        while current:
            print(current.data, end=" ~ ")
            current = current.next
        print(None)

    def length(self):
        """Counts the number of nodes."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def append(self, data):
        """Adds a new node to the end."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        """Adds a new node to the beginning."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def reverse(self):
        """Reverses the order of nodes. Handles empty/single node."""
        if self.is_empty() or not self.head.next:
            return
        current, prev = self.head, None
        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse next pointer
            current.prev = next_node  # Reverse prev pointer
            prev = current  # Move prev pointer
            current = next_node  # Move current pointer
        self.head = prev  # Update head to last node



dll = DoublyLinkedList()
dll.append(12)
dll.append(13)
dll.prepend(11)
dll.display()  # Output: 11 ~ 12 ~ 13 ~ None
dll.reverse()
dll.display()  # Output: 13 ~ 12 ~ 11 ~ None