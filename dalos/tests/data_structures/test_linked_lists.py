import unittest

from dalos.data_structures.linked_lists import SinglyLinkedList, DoublyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
       self.singly_linked_list = SinglyLinkedList()

    def test_append_increments_list_size(self):
        self.singly_linked_list.append(42)
        self.assertEqual(1, len(self.singly_linked_list))

        self.singly_linked_list.append(43)
        self.assertEqual(2, len(self.singly_linked_list))

        self.singly_linked_list.append(44)
        self.assertEqual(3, len(self.singly_linked_list))

    def test_append_adds_node_to_empty_list(self):
        self.singly_linked_list.append(42)

        self.assertEqual(42, self.singly_linked_list.head.data)

    def test_append_sets_list_head_to_list_tail_when_appending_to_empty_list(self):
        self.singly_linked_list.append(42)

        self.assertIs(self.singly_linked_list.head, self.singly_linked_list.tail)

    def test_append_adds_nodes_to_list_tail_and_updates_tail(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)

        self.assertEqual(44, self.singly_linked_list.tail.data)

    def test_append_does_not_update_list_head_when_appending_to_non_empty_list(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)

        self.assertEqual(42, self.singly_linked_list.head.data)

    def test_pop_raises_index_error_when_list_is_empty(self):
        with self.assertRaisesRegex(IndexError, 'pop from empty list'):
            self.singly_linked_list.pop()

    def test_pop_raises_index_error_when_index_out_of_range(self):
        self.singly_linked_list.append(42)

        with self.assertRaisesRegex(IndexError, 'pop index out of range'):
            self.singly_linked_list.pop(2)

    def test_pop_decrements_list_size(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)

        self.singly_linked_list.pop()
        self.assertEqual(2, len(self.singly_linked_list))

        self.singly_linked_list.pop()
        self.assertEqual(1, len(self.singly_linked_list))

        self.singly_linked_list.pop()
        self.assertEqual(0, len(self.singly_linked_list))

    def test_pop_removes_head_and_tail_from_list_of_size_one(self):
        self.singly_linked_list.append(42)

        self.singly_linked_list.pop()

        self.assertIsNone(self.singly_linked_list.head)
        self.assertIsNone(self.singly_linked_list.tail)

    def test_pop_removes_and_updates_list_tail_when_index_is_not_given(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)

        self.singly_linked_list.pop()

        self.assertEqual(43, self.singly_linked_list.tail.data)

    def test_pop_removes_and_updates_list_head_when_index_is_zero(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)

        self.singly_linked_list.pop(0)

        self.assertEqual(43, self.singly_linked_list.head.data)

    def test_pop_removes_and_updates_list_tail_when_index_is_list_size_minus_one(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)

        self.singly_linked_list.pop(2)

        self.assertEqual(43, self.singly_linked_list.tail.data)

    def test_pop_returns_popped_node_with_next_node_none(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)

        popped_node = self.singly_linked_list.pop(1)

        self.assertEqual(43, popped_node.data)
        self.assertIsNone(popped_node.next_node)

    def test_insert_inserts_node_at_list_head_when_list_is_empty(self):
        self.singly_linked_list.insert(0, 42)

        self.assertIs(42, self.singly_linked_list.head.data)

    def test_insert_sets_list_head_to_list_tail_when_inserting_into_empty_list(self):
        self.singly_linked_list.insert(0, 42)

        self.assertIs(self.singly_linked_list.tail, self.singly_linked_list.head)

    def test_insert_inserts_node_at_head_when_index_is_zero_and_list_not_empty(self):
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)

        self.singly_linked_list.insert(0, 42)

        self.assertIs(42, self.singly_linked_list.head.data)
        self.assertIs(44, self.singly_linked_list.tail.data)

    def test_insert_inserts_node_at_index_when_index_is_between_zero_and_list_size(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(44)
        self.singly_linked_list.append(45)

        insert_location = 1
        self.singly_linked_list.insert(insert_location, 43)

        node_before_inserted_node = self.singly_linked_list.head
        for _ in range(insert_location):
            node_before_inserted_node = node_before_inserted_node.next_node

        self.assertEqual(43, node_before_inserted_node.next_node.data)
        self.assertEqual(45, node_before_inserted_node.next_node.next_node.data)

    def test_insert_inserts_node_at_list_tail_when_index_is_greater_than_list_size(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)

        self.singly_linked_list.insert(4, 45)

        self.assertEqual(45, self.singly_linked_list.tail.data)

    def test_insert_inserts_node_at_abs_index_when_index_is_negative(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(45)

        insert_location = -2
        node_before_inserted_node = self.singly_linked_list.head
        for _ in range(abs(insert_location)):
            node_before_inserted_node = node_before_inserted_node.next_node

        self.singly_linked_list.insert(-2, 44)

        self.assertEqual(44, node_before_inserted_node.next_node.data)

    def test_find_returns_none_when_list_is_empty(self):
        node = self.singly_linked_list.find(42)

        self.assertIsNone(node)

    def test_find_returns_none_when_node_not_found(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(43)
        self.singly_linked_list.append(44)

        node = self.singly_linked_list.find(45)

        self.assertIsNone(node)

    def test_find_returns_first_occurrence_of_node_with_matching_data(self):
        self.singly_linked_list.append(42)
        self.singly_linked_list.append(45)
        self.singly_linked_list.append(44)
        self.singly_linked_list.append(45)

        node = self.singly_linked_list.find(45)

        self.assertEqual(45, node.data)
        self.assertIsNot(node, self.singly_linked_list.tail)

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
