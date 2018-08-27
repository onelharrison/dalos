from abc import ABC, abstractmethod

class LinkedList(ABC):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    @abstractmethod
    def append(self, data):
        raise NotImplementedError

    @abstractmethod
    def pop(self, pos=None):
        raise NotImplementedError

    @abstractmethod
    def delete(self, data):
        raise NotImplementedError

    @abstractmethod
    def find(self, data):
        raise NotImplementedError

    @abstractmethod
    def insert_at(self, data, pos):
        raise NotImplementedError

    def __len__(self):
        return self.size

class LinkedListNode:
    def __init__(self, data):
        self.data = data

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
        if self.size == 0:
            raise IndexError('pop from empty list') 

        if index and index > self.size - 1:
            raise IndexError('pop index out of range')

        pos = self.size - 1 if index is None else index

        current_node = self.head
        for _ in range(pos - 1):
            current_node = current_node.next_node

        if self.size == 1:
            current_node = None
            self.head = current_node
        else:
            current_node.next_node = current_node.next_node.next_node

        self.size -= 1
        if index is None:
            self.tail = current_node

    def delete(self, data):
        return

    def find(self, data):
        return

    def insert_at(self, data, pos):
        return 

class SinglyLinkedListNode(LinkedListNode):
    def __init__(self, data=None):
        super().__init__(data)
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

    def pop(self, pos):
        return

    def delete(self, data):
        return

    def find(self, data):
        return

    def insert_at(self, data, pos):
        return

    def prepend(self, data):
        return

class DoublyLinkedListNode(LinkedListNode):
    def __init__(self, data=None):
        super().__init__(data)
        self.prev_node = None
        self.next_node = None
