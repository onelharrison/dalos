from abc import ABC, abstractmethod

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
    def insert_at(self, data, pos):
        raise NotImplementedError

    def __len__(self):
        return self.size

class LinkedListNode(ABC):
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
        super().pop(index)

        pos = self.size - 2 if index is None else index - 1

        current_node = self.head
        for _ in range(pos):
            current_node = current_node.next_node

        if current_node is self.head:
            self.head = current_node.next_node
        else:
            current_node.next_node = current_node.next_node.next_node

        current_node = None if self.size == 1 else current_node

        if index is None or index == self.size - 1:
            self.tail = current_node

        self.size -= 1

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

    def pop(self, index=None):
        super().pop(index)

        pos = self.size - 1 if index is None else index

        current_node = self.head
        for _ in range(pos - 1):
            current_node = current_node.next_node

        if current_node is self.head:
            self.head = current_node.next_node
            if self.head is not None:
                self.head.prev_node = None
        else:
            current_node.next_node = current_node.next_node.next_node
            if current_node.next_node is not None:
                current_node.next_node.prev_node = current_node

        current_node = None if self.size == 1 else current_node

        if index is None or index == self.size - 1:
            self.tail = current_node

        self.size -= 1

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
