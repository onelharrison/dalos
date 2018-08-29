import unittest

from dalos.data_structures.linked_lists import SinglyLinkedList, DoublyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
       self.singly_linked_list = SinglyLinkedList()

    def test_append_when_list_is_empty(self):
        self.singly_linked_list.append(42)

        self.assertEqual(1, len(self.singly_linked_list))
        self.assertEqual(42, self.singly_linked_list.head.data)
        self.assertIs(self.singly_linked_list.head, self.singly_linked_list.tail)

    def test_append_when_list_is_not_empty(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)

        self.assertEqual(2, len(self.singly_linked_list))
        self.assertEqual(42, self.singly_linked_list.head.data)
        self.assertEqual(43, self.singly_linked_list.tail.data)

    def test_pop_when_list_is_empty(self):
        with self.assertRaisesRegex(IndexError, 'pop from empty list'):
            self.singly_linked_list.pop()

    def test_pop_when_index_out_of_range(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        with self.assertRaisesRegex(IndexError, 'pop index out of range'):
            self.singly_linked_list.pop(3)

    def test_pop_when_list_size_is_one_and_index_is_not_given(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.pop()

        self.assertEqual(0, len(self.singly_linked_list))
        self.assertIsNone(self.singly_linked_list.head)
        self.assertIsNone(self.singly_linked_list.tail)

    def test_pop_when_list_size_is_two_and_index_is_not_given(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.pop()

        self.assertEqual(1, len(self.singly_linked_list))
        self.assertEqual(42, self.singly_linked_list.tail.data)

    def test_pop_when_list_size_is_three_and_index_is_not_given(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)
        self.singly_linked_list.pop()

        self.assertEqual(2, len(self.singly_linked_list))
        self.assertEqual(43, self.singly_linked_list.tail.data)

    def test_pop_when_index_given_is_for_list_head(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)
        self.singly_linked_list.pop(0)

        self.assertEqual(2, len(self.singly_linked_list))
        self.assertEqual(43, self.singly_linked_list.head.data)

    def test_pop_when_index_given_is_for_list_tail(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)
        self.singly_linked_list.pop(2)

        self.assertEqual(2, len(self.singly_linked_list))
        self.assertEqual(43, self.singly_linked_list.tail.data)

    def test_pop_returns_popped_node_with_next_node_none(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)

        popped_node = self.singly_linked_list.pop(1)

        self.assertEqual(2, len(self.singly_linked_list))
        self.assertEqual(43, popped_node.data)
        self.assertIsNone(popped_node.next_node)
         
class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.doubly_linked_list = DoublyLinkedList()

    def test_append_when_list_is_empty(self):
        self.doubly_linked_list.append(42)

        self.assertEqual(1, len(self.doubly_linked_list))
        self.assertEqual(42, self.doubly_linked_list.head.data)
        self.assertEqual(self.doubly_linked_list.head, self.doubly_linked_list.tail)

    def test_append_when_list_is_not_empty(self):
        self.doubly_linked_list.append(42)
        self.doubly_linked_list.append(43)

        self.assertEqual(2, len(self.doubly_linked_list))
        self.assertEqual(42, self.doubly_linked_list.head.data)
        self.assertEqual(43, self.doubly_linked_list.tail.data)
        self.assertEqual(self.doubly_linked_list.tail.prev_node, self.doubly_linked_list.head)

    def test_pop_when_list_is_empty(self):
        with self.assertRaisesRegex(IndexError, 'pop from empty list'):
            self.doubly_linked_list.pop()

    def test_pop_when_index_out_of_range(self):
        self.doubly_linked_list.append(42)
        self.doubly_linked_list.append(43)
        with self.assertRaisesRegex(IndexError, 'pop index out of range'):
            self.doubly_linked_list.pop(3)

    def test_pop_when_list_size_is_one_and_index_is_not_given(self):
        self.doubly_linked_list.append(42)
        self.doubly_linked_list.pop()

        self.assertEqual(0, len(self.doubly_linked_list))
        self.assertIsNone(self.doubly_linked_list.head)
        self.assertIsNone(self.doubly_linked_list.tail)

    def test_pop_when_list_size_is_two_and_index_is_not_given(self):
        self.doubly_linked_list.append(42)
        self.doubly_linked_list.append(43)
        self.doubly_linked_list.pop()

        self.assertEqual(1, len(self.doubly_linked_list))
        self.assertEqual(42, self.doubly_linked_list.tail.data)

    def test_pop_when_list_size_is_three_and_index_is_not_given(self):
        self.doubly_linked_list.append(42)
        self.doubly_linked_list.append(43)
        self.doubly_linked_list.append(44)
        self.doubly_linked_list.pop()

        self.assertEqual(2, len(self.doubly_linked_list))
        self.assertEqual(43, self.doubly_linked_list.tail.data)

    def test_pop_when_list_size_is_three_and_index_given_is_between_other_nodes(self):
        self.doubly_linked_list.append(42)
        self.doubly_linked_list.append(43)
        self.doubly_linked_list.append(44)
        self.doubly_linked_list.pop(1)

        self.assertEqual(2, len(self.doubly_linked_list))
        self.assertEqual(42, self.doubly_linked_list.head.data)
        self.assertEqual(44, self.doubly_linked_list.tail.data)
        self.assertIs(self.doubly_linked_list.head.next_node, self.doubly_linked_list.tail)
        self.assertIs(self.doubly_linked_list.head, self.doubly_linked_list.tail.prev_node)

    def test_pop_when_index_given_is_for_list_head(self):
        self.doubly_linked_list.append(42)
        self.doubly_linked_list.append(43)
        self.doubly_linked_list.append(44)
        self.doubly_linked_list.pop(0)

        self.assertEqual(2, len(self.doubly_linked_list))
        self.assertEqual(43, self.doubly_linked_list.head.data)
        self.assertIsNone(self.doubly_linked_list.head.prev_node)

    def test_pop_when_index_given_is_for_list_tail(self):
        self.doubly_linked_list.append(42)
        self.doubly_linked_list.append(43)
        self.doubly_linked_list.append(44)
        self.doubly_linked_list.pop(2)

        self.assertEqual(2, len(self.doubly_linked_list))
        self.assertEqual(43, self.doubly_linked_list.tail.data)
        self.assertIsNone(self.doubly_linked_list.tail.next_node)

    def test_pop_returns_popped_node_with_prev_and_next_node_none(self):
        self.doubly_linked_list.append(42)
        self.doubly_linked_list.append(43)
        self.doubly_linked_list.append(44)

        popped_node = self.doubly_linked_list.pop(1)

        self.assertEqual(2, len(self.doubly_linked_list))
        self.assertEqual(43, popped_node.data)
        self.assertIsNone(popped_node.prev_node)
        self.assertIsNone(popped_node.next_node)

if __name__ == '__main__':
    unittest.main()
