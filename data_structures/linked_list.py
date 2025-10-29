class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        O(1) -> no matter many nodes there are, number of operations needed to add one
                more item is always the same
        """
        # Create new node
        new_node = Node(value)
        if self.head is None:
            # Handle edge case: empty list
            self.head = new_node
            self.tail = new_node
        else:
            # Have last item point to it
            self.tail.next = new_node
            # Have tail point to it
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        O(n) -> need to iterate over all nodes
        """
        # Handle edge case: empty list
        if self.length == 0:
            return None
        # Set pointes to head
        temp = self.head
        pre = self.head
        # Reach last node with temp (pre points to one node before)
        while temp.next is not None:
            pre = temp
            temp = temp.next
        # Have tail point to new last node
        self.tail = pre
        # Have the new last node point to none
        self.tail.next = None
        self.length -= 1
        # Handle edge case: list was originally with one item (now left empty)
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        """
        O(1) -> no matter many nodes there are, number of operations needed to add one
                more item in front of the current head is always the same
        """
        # Create new node
        new_node = Node(value)
        # Have it point to current head
        new_node.next = self.head
        # Have head point to the new node
        self.head = new_node
        # Handle edge case: empty list
        if self.length == 0:
            self.tail = new_node
        self.length += 1
        return True

    def pop_first(self):
        """
        O(1) -> no matter the number of nodes, we just remove the first one
        """
        # Handle edge case: empty list
        if self.length == 0:
            return None
        # Store current head in pointed temp
        temp = self.head
        # Move head to the second node
        self.head = self.head.next
        # Have temp point to noen
        temp.next = None
        self.length -= 1
        # Handle edge case: list was originally with one item (now left empty)
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        """
        O(n) -> need to iterate over all nodes in the worst case
        """
        # Handle edge case: index out of bounds
        if index < 0 or index >= self.length:
            return None
        # Set pointer to head
        temp = self.head
        # Reach node at index and return it
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """
        O(n) -> need to iterate over all nodes in the worst case
        """
        # Get the node at index
        temp = self.get(index)
        # Overwrite node's value (if it exists)
        if temp:
            temp.value = value
            return True
        # Return False if node does not exist at index (index out of bounds)
        return False

    def insert(self, index, value):
        """
        O(n) -> need to reach node at index-1, iterating through the list
        """
        # Handle edge case: index out of bounds
        if index < 0 or index > self.length:
            return False
        # Handle edge case: index is 0, prepend
        if index == 0:
            return self.prepend(value)
        # Handle edge case: index is length, append
        if index == self.length:
            return self.append(value)
        # Create new node
        new_node = Node(value)
        # Create pointer to the node previous to the one at index
        temp = self.get(index - 1)
        # Have new node point at subsequent node
        new_node.next = temp.next
        # Have previous node point at the new inserted node
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        O(n) -> need to reach node at index, iterating through the list
        """
        # Handle edge case: index out of bounds
        if index < 0 or index >= self.length:
            return None
        # Handle edge case: index is 0, pop first
        if index == 0:
            return self.pop_first()
        # Handle edge case: index is length, pop
        if index == self.length - 1:
            return self.pop()
        # Create pointers to the node previous to the one at index, and the one at index
        prev = self.get(index - 1)
        temp = prev.next
        # Make it point to the subsequent node
        prev.next = temp.next
        # Make the removed node point to none
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        # Swap head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # Create pointers to the previous and next node
        prev = None
        next = temp.next
        # Iterate over list and reverse pointers
        for _ in range(self.length):
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next




ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)


