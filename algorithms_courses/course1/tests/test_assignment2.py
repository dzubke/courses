# tests for the assignment2.py functions

import unittest
import sys
sys.path.insert(1, '/Users/dustin/CS/projects/courses/algorithms_course/assignment2')

from assignment2 import sort_count

class TestAssignment2(unittest.TestCase):


    def test_sort_count(self):
        '''Tests the sort count function with a variety of list contexts

        '''

        int_list_1 = [1, 2, 3]
        sort_count_1_list, sort_count_1_count  = sort_count(int_list_1)
        self.assertEqual(sort_count_1_list, [1, 2, 3])
        self.assertEqual(sort_count_1_count, 0)

        # ensure the function outputs the correct types
        self.assertIsInstance(sort_count_1_count, int)
        self.assertIsInstance(sort_count_1_list, list)
        
        int_list_2 = [1, 5, 4, 3, 2]
        sort_count_2_list, sort_count_2_count  = sort_count(int_list_2)
        self.assertEqual(sort_count_2_list, [1, 2, 3, 4, 5])
        self.assertEqual(sort_count_2_count, 6)

        int_list_3 = [1]
        sort_count_3_list, sort_count_3_count  = sort_count(int_list_3)
        self.assertEqual(sort_count_3_list, [1])
        self.assertEqual(sort_count_3_count, 0)

        int_list_4 = []
        sort_count_4_list, sort_count_4_count  = sort_count(int_list_4)
        self.assertEqual(sort_count_4_list, [])
        self.assertEqual(sort_count_4_count, 0)

        int_list_5 = [9,8,7,6,5,4,3,2,1]
        sort_count_5_list, sort_count_5_count  = sort_count(int_list_5)
        self.assertEqual(sort_count_5_list, [1,2,3,4,5,6,7,8,9])
        self.assertEqual(sort_count_5_count, 36)
   