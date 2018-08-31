from abc import ABC, abstractmethod

class LinkedListNode(ABC):
    def __init__(self, data):
        self.data = data

class LinkedList(ABC):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    @abstractmethod
    def append(self, data):
        raise NotImplementedError

    def pop(self, index=None):
        if self.size == 0:
            raise IndexError('pop from empty list') 

        if index and index > self.size - 1:
            raise IndexError('pop index out of range')

    @abstractmethod
    def delete(self, data):
        raise NotImplementedError

    @abstractmethod
    def find(self, data):
        raise NotImplementedError

    @abstractmethod
    def insert(self, index, data):
        raise NotImplementedError

    def __len__(self):
        return self.size

class SinglyLinkedListNode(LinkedListNode):
    def __init__(self, data=None):
        super().__init__(data)
        self.next_node = None

class SinglyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def append(self, data):
        node = SinglyLinkedListNode(data)
        if self.head is None:
           self.head = node

        if self.tail:
           self.tail.next_node = node

        self.tail = node
        self.size += 1

    def pop(self, index=None):
        super().pop(index)

        dummy_head = SinglyLinkedListNode()
        dummy_head.next_node = self.head

        pop_location = self.size - 1 if index is None else index

        current_node = dummy_head
        for _ in range(pop_location):
            current_node = current_node.next_node

        popped_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node

        if pop_location == 0:
            current_node = current_node.next_node
            self.head = current_node

        if pop_location == self.size - 1:
            self.tail = current_node

        self.size -= 1

        popped_node.next_node = None

        return popped_node

    def insert(self, index, data):
        insert_location = index if index <= self.size else self.size

        current_node = self.head
        for _ in range(insert_location):
            current_node = current_node.next_node

        insert_node = SinglyLinkedListNode(data)

        if insert_location == 0:
            self.head = insert_node

        if insert_location == self.size:
            self.tail = insert_node

        if current_node:
            insert_node.next_node = current_node.next_node
            current_node.next_node = insert_node

        self.size += 1

    def delete(self, data):
        return

    def find(self, data):
       current_node = self.head 
       while current_node and current_node.data != data:
           current_node = current_node.next_node

       return current_node

class DoublyLinkedListNode(LinkedListNode):
    def __init__(self, data=None):
        super().__init__(data)
        self.prev_node = None
        self.next_node = None

class DoublyLinkedList(LinkedList):
    def __init__(self, data=None):
        super().__init__()

    def append(self, data):
        node = DoublyLinkedListNode(data)
        if self.head is None:
           self.head = node

        if self.tail:
           node.prev_node = self.tail
           self.tail.next_node = node

        self.tail = node
        self.size += 1

    def pop(self, index=None):
        super().pop(index)

        dummy_head = DoublyLinkedListNode()
        dummy_head.next_node = self.head

        pop_location = self.size - 1 if index is None else index

        current_node = dummy_head
        for _ in range(pop_location):
            current_node = current_node.next_node

        popped_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node

        if current_node.next_node:
            current_node.next_node.prev_node = current_node

        if pop_location == 0:
            current_node = current_node.next_node
            if current_node:
                current_node.prev_node = None
            self.head = current_node

        if pop_location == self.size - 1:
            self.tail = current_node

        self.size -= 1

        popped_node.prev_node = None
        popped_node.next_node = None

        return popped_node

    def delete(self, data):
        return

    def find(self, data):
        return

    def insert(self, index, data):
        return

