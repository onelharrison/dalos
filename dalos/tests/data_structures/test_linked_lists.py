import unittest

from dalos.data_structures import linked_lists as ll

class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
       self.singlyLinkedList = ll.SinglyLinkedList()

    def test_append_when_list_is_empty(self):
        self.singlyLinkedList.append(42)

        self.assertEqual(1, len(self.singlyLinkedList))
        self.assertEqual(42, self.singlyLinkedList.head.data)
        self.assertIs(self.singlyLinkedList.head, self.singlyLinkedList.tail)

    def test_append_when_list_is_not_empty(self):
        self.singlyLinkedList.append(42)
        self.singlyLinkedList.append(43)

        self.assertEqual(2, len(self.singlyLinkedList))
        self.assertEqual(42, self.singlyLinkedList.head.data)
        self.assertEqual(43, self.singlyLinkedList.tail.data)

    def test_pop_when_list_is_empty(self):
        with self.assertRaisesRegex(IndexError, 'pop from empty list'):
            self.singlyLinkedList.pop()

    def test_pop_when_index_out_of_range(self):
        self.singlyLinkedList.append(42)
        self.singlyLinkedList.append(43)
        with self.assertRaisesRegex(IndexError, 'pop index out of range'):
            self.singlyLinkedList.pop(3)

    def test_pop_when_list_size_is_one_and_index_is_not_given(self):
        self.singlyLinkedList.append(42)
        self.singlyLinkedList.pop()

        self.assertEqual(0, len(self.singlyLinkedList))
        self.assertIsNone(self.singlyLinkedList.head)
        self.assertIsNone(self.singlyLinkedList.tail)

    def test_pop_when_list_size_is_two_and_index_is_not_given(self):
        self.singlyLinkedList.append(42)
        self.singlyLinkedList.append(43)
        self.singlyLinkedList.pop()

        self.assertEqual(1, len(self.singlyLinkedList))
        self.assertEqual(42, self.singlyLinkedList.tail.data)

    def test_pop_when_list_size_is_three_and_index_is_not_given(self):
        self.singlyLinkedList.append(42)
        self.singlyLinkedList.append(43)
        self.singlyLinkedList.append(44)
        self.singlyLinkedList.pop()

        self.assertEqual(2, len(self.singlyLinkedList))
        self.assertEqual(43, self.singlyLinkedList.tail.data)

class TestDoublyLinkedList(unittest.TestCase):
    def test_append_when_doubly_linked_list_is_empty(self):
        doublyLinkedList = ll.DoublyLinkedList()
        doublyLinkedList.append(42)

        self.assertEqual(1, len(doublyLinkedList))
        self.assertEqual(42, doublyLinkedList.head.data)
        self.assertEqual(doublyLinkedList.head, doublyLinkedList.tail)

    def test_append_when_doubly_linked_list_is_not_empty(self):
        doublyLinkedList = ll.DoublyLinkedList()
        doublyLinkedList.append(42)
        doublyLinkedList.append(43)

        self.assertEqual(2, len(doublyLinkedList))
        self.assertEqual(42, doublyLinkedList.head.data)
        self.assertEqual(43, doublyLinkedList.tail.data)
        self.assertEqual(doublyLinkedList.tail.prev_node, doublyLinkedList.head)

if __name__ == '__main__':
    unittest.main()
