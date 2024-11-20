import group
import unittest
class TestCases(unittest.TestCase):

    def test_groups_of_3_full(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = group.groups_of_3(input_list)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], [1, 2, 3])
        self.assertEqual(result[1], [4, 5, 6])
        self.assertEqual(result[2], [7, 8, 9])

    def test_groups_of_3_partial(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8]]
        result = group.groups_of_3(input_list)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], [1, 2, 3])
        self.assertEqual(result[1], [4, 5, 6])
        self.assertEqual(result[2], [7, 8])




if __name__ == '__main__':
    unittest.main()
