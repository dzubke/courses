#I would like to turn the print in the mergesort.py into unit tests
#having done it for the split function, I could continue to do so for the rest of the functions
#in mergesort.py but I am not going to do so because there are other things I want to do

import unittest
import sys
sys.path.insert(1, '/Users/dustin/CS/projects/algorithms_course/mergesort')

from mergesort import split

class TestMergeSort(unittest.TestCase):


    def test_split(self):
        '''Tests the split function with a variety of list contexts

        '''

        #list of odd length
        split_test_in_list_odd = [1, 2, 3]
        split_test_out_lists_odd = split(split_test_in_list_odd)
        self.assertEqual(split_test_out_lists_odd, ([1], [2, 3]))

        #list of even length
        split_test_in_list_even = [1, 2, 3, 4]
        split_test_out_lists_even = split(split_test_in_list_even)
        self.assertEqual(split_test_out_lists_even, ([1, 2], [3, 4]))

        #list of single value
        split_test_in_list_single = [1]
        split_test_out_lists_single = split(split_test_in_list_single)
        self.assertEqual(split_test_out_lists_single, ([], [1]))

         #testing an empty list
        split_test_in_list_empty = []
        split_test_out_lists_empty = split(split_test_in_list_empty)
        self.assertEqual(split_test_out_lists_empty, ([], []))



if __name__ == '__main__':
    unittest.main()
    
    '''
    #testing the split function

    #testing the merge_sorted_list function
    #two lists of even length
    left_list_1 = [1, 2]
    right_list_1 = [3,4]
    merged_list_1 = merge_sorted_list(left_list_1, right_list_1)
    #two lists of odd length
    left_list_2 = [1]
    right_list_2 = [3, 4, 5]
    merged_list_2 = merge_sorted_list(left_list_2, right_list_2)
    #two lists of mixed length and order
    left_list_3 = [2, 5]
    right_list_3 = [1, 4, 6]
    merged_list_3 = merge_sorted_list(left_list_3, right_list_3)
    #two lists of the same elements
    left_list_4 = [2, 2]
    right_list_4 = [2, 2, 2]
    merged_list_4 = merge_sorted_list(left_list_4, right_list_4)
    #left empty list
    left_list_5 = []
    right_list_5 = [2, 3, 4]
    merged_list_5 = merge_sorted_list(left_list_5, right_list_5)
    #right empty list
    left_list_6 = [1,5,6]
    right_list_6 = []
    merged_list_6 = merge_sorted_list(left_list_6, right_list_6)
    #two empty list
    left_list_7 = []
    right_list_7 = []
    merged_list_7 = merge_sorted_list(left_list_7, right_list_7)
    #single element lists 
    left_list_8 = [1]
    right_list_8 = [2]
    merged_list_8 = merge_sorted_list(left_list_8, right_list_8)
    print('Testing the merge_sorted_list function')
    print(f'Testing two lists of even length: {left_list_1} and {right_list_1} merged into {merged_list_1}' )
    print(f'Testing two lists of odd length: {left_list_2} and {right_list_2} merged into {merged_list_2}' )
    print(f'Testing two lists of mixed length and order: {left_list_3} and {right_list_3} merged into {merged_list_3}' )
    print(f'Testing two lists of the same elements: {left_list_4} and {right_list_4} merged into {merged_list_4}' )
    print(f'Testing left empty list: {left_list_5} and {right_list_5} merged into {merged_list_5}' )
    print(f'Testing right empty list: {left_list_6} and {right_list_6} merged into {merged_list_6}' )
    print(f'Testing two empty list: {left_list_7} and {right_list_7} merged into {merged_list_7}' )
    print(f'Testing single element lists: {left_list_8} and {right_list_8} merged into {merged_list_8}' )
    print('')


    #Testing the merge_sort function
    #Testing a list of even length
    merge_sort_test_in_list_1 = [4, 7, 2, 8]
    merge_sort_test_out_list_1 = merge_sort(merge_sort_test_in_list_1)
    #Testing a list of odd length
    merge_sort_test_in_list_2 = [74, 57, 62]
    merge_sort_test_out_list_2 = merge_sort(merge_sort_test_in_list_2)
    #Testing an empty list
    merge_sort_test_in_list_3 = []
    merge_sort_test_out_list_3 = merge_sort(merge_sort_test_in_list_3)
    #Testing a single element list
    merge_sort_test_in_list_4 = [1]
    merge_sort_test_out_list_4 = merge_sort(merge_sort_test_in_list_4)

    print('Testing the merge_sort function')
    print(f'Testing a list of even length: {merge_sort_test_in_list_1} sorted as {merge_sort_test_out_list_1}' )
    print(f'Testing a list of odd length: {merge_sort_test_in_list_2} sorted as {merge_sort_test_out_list_2}' )
    print(f'Testing an empty list: {merge_sort_test_in_list_3} sorted as {merge_sort_test_out_list_3}' )
    print(f'Testing a single element list: {merge_sort_test_in_list_4} sorted as {merge_sort_test_out_list_4}' )

    '''