# assignment3.py

# standard libraries
from typing import List
from statistics import median
from math import ceil

class QuickSort():
    """This class will implement the quicksort algorithm"""

    def __init__(self, in_list: List) -> None:
        self.list: List = in_list       # list to be sorted
        self.length: int = len(self.list)     # the length of the list object


    def quicksort(self, pivot_pick: str ='first') -> None:
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

        # base case
        if self.length <= 1:                      # if there is one or zero elements in the in_list
            return self.list                      # return the list object

        if pivot_pick == 'first':       # if the pivot picking method is 'first'
            pass                        # then set the pivot as the first element

        elif pivot_pick == 'last':          # if the pivot memthod is 'last'
            self.swap(0, self.length - 1)            # then set the pivot as the last element

        elif pivot_pick =='median':                            # if the pivot choosing method is 'median-of-three'
            # the pivot will be the median of the first, middle, and last elements
            median_pivot = median([self.list[0], self.list[ ceil(self.length/2) - 1 ], self.list[-1] ] )      
            self.swap(0, self.list.index(median_pivot))

        else:   # if pivot_pick is not equal to 'first', 'last', or 'median-of-three' raise the ValueError
            raise ValueError("invalid entry for pivot_pick argument. Valid entries are 1) 'first', 2) 'last', or 3) 'median'")
        
        pivot_index = self.partition(0, self.length)

        leftlist = QuickSort(self.list[:pivot_index-1])

        leftlist.quicksort(pivot_pick = pivot_pick)

        self.list[:pivot_index-1] = leftlist.list

        rightlist = QuickSort(self.list[pivot_index:])

        rightlist.quicksort(pivot_pick = pivot_pick)

        self.list[pivot_index:] = rightlist.list



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

        i = l_index +1              # the i-th index that separates values less than (<i) and greater (>i) of the pivot

        for j in range(i, r_index):
            
            if self.list[j] < pivot:     # if the j-th element is less than the pivot 
                self.swap(i, j)          # swap the i-th element with the j-th element since i is boundary index and the i-th element is greater than the pivot
                i += 1                   # increment i

        self.swap(l_index, i-1)   #after the loop has sorted the array, swap with pivot into place

        return i-1      # returns the index of the pivot for use in the quicksort recursion


        
    def swap(self, index1: int, index2: int):
        """This method will swap the elements in index1 and index2 with three steps:
            1) by appending the value in index1 to the end of the list,
            2) assigning the value in index2 to index1, 
            3) assigning the appended to the end of the list in index2, 
            4) removing the appended element so that the list is the input length.

        Parameters
        ----------
        self: List of length m
            the list in which exists the elements to be swapped as specified in index1 and index2 

        index1: int
            the index of the first element to be swapped.

        index2: int
            the index of the second element to be swapped.

        """

        self.list.append(self.list[index1])     # appending the element in index1 to the end of the list
        self.list[index1] = self.list[index2]   # assigning the value in index2 to index1
        self.list[index2] = self.list[-1]       # assigns the appended value from the input index1 to the value of index2
        del self.list[-1]                       # deletes the appended from index1 from the end of the list


def main():
    in_list = [3, 6, 7, 8, 11, 4, 5, 1, 9]

    print(in_list)

    sortlist = QuickSort(in_list)

    # testing length object
    print(f"the list length is: {sortlist.length}")

    # testing the swap method
    print('\ntesting the swap method')
    sortlist.swap(0, 2)
    print(sortlist.list)

    sortlist.swap(0, sortlist.length-1)
    print(sortlist.list)

    sortlist.swap(3, 5)
    print(sortlist.list)

    # testing quicksort method
    print('\ntesting the quicksort method')
    sortlist.quicksort(pivot_pick = 'first')
    print(sortlist.list)

    sortlist.quicksort(pivot_pick = 'last')
    print(sortlist.list)

    sortlist.quicksort(pivot_pick = 'median')
    print(sortlist.list)

    # testing partition method
    print('\ntesting the partition method')
    sortlist.partition(0, sortlist.length)
    print(sortlist.list)







    


if __name__ == "__main__": main()

"""SCRATCH

        # both indicies below begin at one because the 0-th element in the array is the pivot
        i = 1       # index between which the lists are going to be split along the pivot.
        j = 1       # the index that signifies what portion of the array has been searched over

        while j < self.length:
            
            
            j += 1      # increment j for the next pass of the loop

"""