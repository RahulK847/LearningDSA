# linked List Implementation in Python:
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, position, data):
        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        count = 1

        while count < position - 1 and current:
            current = current.next
            count += 1

        if not current:
            print("Position out of bounds.")
            return

        new_node.next = current.next
        current.next = new_node

    def update_node(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next
        else:
            print(f"Node with data '{old_data}' not found.")

    def delete_node(self, key):
        if self.is_empty():
            print("The list is empty.")
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next
        else:
            print(f"Node with data '{key}' not found.")

    def remove_first_node(self):
        if self.is_empty():
            print("The list is empty.")
            return

        self.head = self.head.next

    def remove_last_node(self):
        if self.is_empty():
            print("The list is empty.")
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next:
            current = current.next

        current = None

    def delete_at_position(self, position):
        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.remove_first_node()
            return

        current = self.head
        count = 1

        while count < position - 1 and current:
            current = current.next
            count += 1

        if not current or not current.next:
            print("Position out of bounds.")
            return

        current.next = current.next.next

    def delete_by_data(self, data):
        if self.is_empty():
            print("The list is empty.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        else:
            print(f"Node with data '{data}' not found.")


# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()

print("Length of the linked list:", linked_list.length())

linked_list.prepend(0)
linked_list.display()

linked_list.insert_at_position(3, 2.5)
linked_list.display()

linked_list.update_node(2, 20)
linked_list.display()

linked_list.delete_node(1)
linked_list.display()

linked_list.remove_first_node()
linked_list.display()

linked_list.remove_last_node()
linked_list.display()

linked_list.delete_at_position(2)
linked_list.display()

linked_list.delete_by_data(20)
linked_list.display()
