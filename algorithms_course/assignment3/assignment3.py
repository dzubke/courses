# assignment3.py
# this is the main implementation as it uses Classes to perform quicksort as this was cooler than not using classes and actually was a bit cleaner. 
# this implementation is very similar to that in assignment3_nonclass.py but it uses a Class for the algorithm implementation.


# standard libraries
from typing import List
from statistics import median
from math import floor

class QuickSort():
    """This class will implement the quicksort algorithm"""

    def __init__(self, in_list: List) -> None:
        self.list: List = in_list       # list to be sorted
        self.length: int = len(self.list)     # the length of the list object
        self.count: int = 0                    # the number of comparisons performed for this object. 


    def quicksort(self, pivot_pick: str ='first') -> int:
        """The Quick Sort recursive sort algorithm where by default the first element of the list is the pivot. Varients on how the pivot elements is choosen
            include: 1) the first element of the list, 2) the last element of the list, and 3) the median-of-three where the pivot is chosen as the median of the
            first, last, and middle elements of the list. 
        
        Parameters
        ----------
        in_list: list
            the input list that will be sorted

        pivot_pick: str
            a string value that specifies what method will be used to pick the pivot element. There are three valid arguments: 1) an argument of 'first' will 
                choose the first element of the in_list as the pivot, 2) an argument of 'last' will choose the last element of the in_list as the pivot, or
                3) an argument of 'median' will choose the median value of the first, last, and middle element as the pivot
        
        Returns
        -------
        nothing: None
            the actions of the method are performed on the QuickSort class object

        """

        self.quicksortHelper(0, self.length, pivot_pick = pivot_pick)

        return self.count

    def quicksortHelper(self, l_index, r_index, pivot_pick = 'first'):
        """A helper function for quicksort in which the resursive calls will be made.
        """
    
        if l_index < r_index: 

            if pivot_pick == 'first':       # if the pivot picking method is 'first'
                pass                        # then set the pivot as the first element

            elif pivot_pick == 'last':          # if the pivot memthod is 'last'
                self._swap(l_index, r_index-1)            # then set the pivot as the last element

            elif pivot_pick =='median':                            # if the pivot choosing method is 'median-of-three'
                # the pivot will be the median of the first, middle, and last elements
                median_index_org = floor( (r_index - 1 + l_index) /2)        # this calculates the index of the median element in the original list
                median_pivot = median([self.list[l_index], self.list[ median_index_org ], self.list[ r_index-1 ] ] ) 

                # then swap whichever value was picked as the median-of-three with the first value in the array
                if median_pivot == self.list[l_index]:
                    pass        # don't do anything because the median is already in the l_index position

                elif median_pivot == self.list[ median_index_org ]:       # if the median in the original list was picked
                    self._swap(l_index, median_index_org)  # swap it with the first element

                elif median_pivot == self.list[ r_index-1 ]:              # if the last element of the list was picked
                    self._swap(l_index, r_index - 1 )      # sswap it with the first element

            else:   # if pivot_pick is not equal to 'first', 'last', or 'median-of-three' raise the ValueError
                raise ValueError("invalid entry for pivot_pick argument. Valid entries are 1) 'first', 2) 'last', or 3) 'median'")

            pivot_index = self.partition(l_index, r_index)
            self.addCounter(r_index - l_index - 1)

            self.quicksortHelper(l_index, pivot_index, pivot_pick=pivot_pick)
            self.quicksortHelper(pivot_index+1, r_index, pivot_pick=pivot_pick)

    
    def addCounter(self, increase: int) -> None:
        """This function increases the count attribute of the QuickSort object

        Parameters
        ----------
        increase: int
            the integer amount the count attribute will be increased

        Returns
        -------
        None
            only increases the count attribute. 

        """
        self.count += increase


    def partition(self, l_index: int, r_index: int) -> int:
        """The partition sub-routine of quicksort. 

        Parameters
        ----------
        self: QuickSort object

        l_index: int
            the left index of the partitioned array within the greater list

        r_index: int
            the right index of the partitioned array with the greater list

        Returns
        -------
        nothing: None
            the actions of the method are performed on the QuickSort class object

        """

        pivot = self.list[l_index]  # the pivot

        i = l_index + 1              # the i-th index that separates values less than (<i) and greater (>i) of the pivot

        for j in range(i, r_index):
            
            if self.list[j] < pivot:     # if the j-th element is less than the pivot 
                self._swap(i, j)          # sswap the i-th element with the j-th element since i is boundary index and the i-th element is greater than the pivot
                i += 1                   # increment i

        self._swap(l_index, i-1)   #after the loop has sorted the array, _swap with pivot into place

        return i-1      # returns the index of the pivot for use in the quicksort recursion


    def _swap(self, index1: int, index2: int):
        """This private method will swap the elements in index1 and index2.
       
        Parameters
        ----------
        in_list: List of length m
            the list in which exists the elements to be swapped as specified in index1 and index2 

        index1: int
            the index of the first element to be swapped.

        index2: int
            the index of the second element to be swapped.

        """

        self.list[index1], self.list[index2] = self.list[index2], self.list[index1] 


def main():
    in_list = [3, 6, 7, 8, 11, 4, 5, 1, 9]

    print(in_list)

    sortlist = QuickSort(in_list)

    # testing length object
    print(f"the list length is: {sortlist.length}")

    # testing the swap method
    print('\ntesting the swap method')
    sortlist._swap(0, 2)
    print(sortlist.list)

    sortlist._swap(0, sortlist.length-1)
    print(sortlist.list)

    sortlist._swap(3, 5)
    print(sortlist.list)

    # testing quicksort method
    print('\ntesting the quicksort method')
    sortlist = QuickSort(in_list)   # reinitializing the object
    sortlist.quicksort(pivot_pick = 'first')
    print(sortlist.list)
    print(f"first count is: {sortlist.count}")

    sortlist = QuickSort(in_list)   # reinitializing the object
    sortlist.quicksort(pivot_pick = 'last')
    print(sortlist.list)
    print(f"last count is: {sortlist.count}")

    sortlist = QuickSort(in_list)   # reinitializing the object
    sortlist.quicksort(pivot_pick = 'median')
    print(sortlist.list)
    print(f"median count is: {sortlist.count}")

    # testing partition method
    print('\ntesting the partition method')
    sortlist.partition(0, sortlist.length)
    print(sortlist.list) 

    
    with open('data_QuickSort.txt', 'r') as f:
        data_list_first = [int(line.strip()) for line in f]
        sortlist = QuickSort(data_list_first)   # initializing the object
    
        print(sortlist.list[:15])
        print(f"data list len: {sortlist.length}")

        sortlist.quicksort(pivot_pick='first')
        print(sortlist.list[:15])
        print(f"the first count is: {sortlist.count}")

        assert sortlist.list  == [x for x in range(1, 10001)]
        assert sortlist.count == 162085
    
    with open('data_QuickSort.txt', 'r') as f:
        data_list_last = [int(line.strip()) for line in f]
        sortlist = QuickSort(data_list_last)   # re-initializing the object

        print(sortlist.list[:15])
        print(f"data last len: {sortlist.length}")

        sortlist.quicksort(pivot_pick='last')
        print(sortlist.list[:15])
        print(f"the last count is: {sortlist.count}")

        assert sortlist.list  == [x for x in range(1, 10001)]
        assert sortlist.count == 164123

    with open('data_QuickSort.txt', 'r') as f:
        data_list_median = [int(line.strip()) for line in f]
        sortlist = QuickSort(data_list_median)   # re-initializing the object

        print(sortlist.list[:15])
        print(f"data last len: {sortlist.length}")

        sortlist.quicksort(pivot_pick='median')
        print(sortlist.list[:15])
        print(f"the  median count is: {sortlist.count}")

        assert sortlist.list  == [x for x in range(1, 10001)]
        assert sortlist.count == 138382
    

if __name__ == "__main__": main()

"""SCRATCH

        # both indicies below begin at one because the 0-th element in the array is the pivot
        i = 1       # index between which the lists are going to be split along the pivot.
        j = 1       # the index that signifies what portion of the array has been searched over

        while j < self.length:
            
            
            j += 1      # increment j for the next pass of the loop

"""