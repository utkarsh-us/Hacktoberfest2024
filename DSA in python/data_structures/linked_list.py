class Node:
    """Class to represent a single node in a linked list."""
    
    def __init__(self, value):
        """
        Initialize a node with a value and no next node.

        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    """Class to represent a linked list."""
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def append(self, value):
        """
        Append a new value to the end of the linked list.

        Args:
            value: The value to be added to the list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            self._append_to_tail(new_node)

    def _append_to_tail(self, new_node):
        """Helper method to append a node to the tail of the list."""
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all values in the linked list."""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        current = self.head
        while current:
            next_node = current.next # Store the next node
            current.next = prev  # Reverse the link
            prev = current       # Move prev to current
            current = next_node  # Move to the next node
        self.head = prev  # Update head to the new first node


def main():
    """Main function to demonstrate linked list operations."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    print("Original list:")
    ll.print_list()

    ll.reverse()
    print("Reversed list:")
    ll.print_list()


if __name__ == "__main__":
    main()
