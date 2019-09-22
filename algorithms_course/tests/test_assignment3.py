# standard libraries 
import unittest
import sys

# project libraries
from assignment3.assignment3 import QuickSort
    

sys.path.insert(1, '/Users/dustin/CS/projects/courses/algorithms_course/assignment3')


class TestQuickSort(unittest.TestCase):

    '''
    def test___init__(self):
        """Tests the __init__ method"""

        # initializing the list objects
        in_list = [3, 6, 7, 8, 2, 4, 5, 1, 9]
        # sortlist = QuickSort(in_list)

        # assert type(sortlist.list) == list, "the object's list attribute is not of list type"
        # assert type(sortlist.length) == int, "the object's length attribute is not of int type"

        # testing length object
        assert len(in_list) == 9, "the object's length object is not correct"
    '''

    def test_swap(self):
        """Tests the swap method"""

        # initializing the list objects
        in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sortlist = QuickSort(in_list)

        sortlist._swap(0, 2)
        self.assertEqual(sortlist.list, [3, 2, 1, 4, 5, 6, 7, 8, 9])

        sortlist._swap(0, sortlist.length-1)
        self.assertEqual(sortlist.list, [9, 2, 1, 4, 5, 6, 7, 8, 3])

        sortlist._swap(3, 5)
        self.assertEqual(sortlist.list, [9, 2, 1, 6, 5, 4, 7, 8, 3])


    def test_quicksort(self):
        """Tests the quicksort method"""

        # initializing the list objects
        in_list = [3, 6, 7, 8, 2, 4, 5, 1, 9]
        sortlist = QuickSort(in_list)

        # testin the 'first' keyword arguement
        sortlist.quicksort(pivot_pick = 'first')
        self.assertEqual(sortlist.list,  [1, 2, 3, 4, 5, 6, 7, 8, 9])

        # testing the 'last' keyword arguement
        sortlist.quicksort(pivot_pick = 'last')
        self.assertEqual(sortlist.list,  [1, 2, 3, 4, 5, 6, 7, 8, 9])

        # testing the 'median' keyword arguement
        sortlist.quicksort(pivot_pick = 'median')
        self.assertEqual(sortlist.list, [1, 2, 3, 4, 5, 6, 7, 8, 9])

        # testing the ValueError clause
        # assert sortlist.quicksort(pivot_pick = 'fun_time') ==  ValueError



        