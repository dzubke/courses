# assignment3.py

# standard libraries
from typing import List, Tuple
from statistics import median
from math import ceil


def quicksort(in_list: List, pivot_pick: str ='first') -> List:
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

    n = len(in_list)                    # lenght of input list

    # base case
    if n <= 1:                      # if there is one or zero elements in the in_list
        return in_list                     # return the list object

    if pivot_pick == 'first':       # if the pivot picking method is 'first'
        pass                        # then set the pivot as the first element

    elif pivot_pick == 'last':          # if the pivot memthod is 'last'
        in_list = swap(in_list, 0, n - 1)            # then set the pivot as the last element

    elif pivot_pick =='median':                            # if the pivot choosing method is 'median-of-three'
        # the pivot will be the median of the first, middle, and last elements
        median_pivot = median([in_list[0], in_list[ ceil(n/2) - 1 ], in_list[-1] ] )      
        in_list = swap(in_list, 0, in_list.index(median_pivot))

    else:   # if pivot_pick is not equal to 'first', 'last', or 'median-of-three' raise the ValueError
        raise ValueError("invalid entry for pivot_pick argument. Valid entries are 1) 'first', 2) 'last', or 3) 'median'")
    
    
    in_list, pivot_index = partition(in_list, 0, n)
    print(f"length of left list: {len(in_list[:pivot_index -1])}")
    print(f"length of right list: {len(in_list[:pivot_index -1])}")


    return quicksort(in_list, ) + [in_list[pivot_index]] + quicksort(in_list[pivot_index:])



def partition(in_list, l_index: int, r_index: int) -> Tuple[List, int]:
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

    pivot = in_list[l_index]  # the pivot

    i = l_index +1              # the i-th index that separates values less than (<i) and greater (>i) of the pivot

    for j in range(i, r_index):
        
        if in_list[j] < pivot:     # if the j-th element is less than the pivot 
            in_list = swap(in_list, i, j)          # swap the i-th element with the j-th element since i is boundary index and the i-th element is greater than the pivot
            i += 1                   # increment i

    in_list = swap(in_list, l_index, i-1)   #after the loop has sorted the array, swap with pivot into place

    return in_list, i-1      # returns the index of the pivot for use in the quicksort recursion


    
def swap(in_list: List, index1: int, index2: int) -> List:
    """This method will swap the elements in index1 and index2 with three steps:
        1) by appending the value in index1 to the end of the list,
        2) assigning the value in index2 to index1, 
        3) assigning the appended to the end of the list in index2, 
        4) removing the appended element so that the list is the input length.

    Parameters
    ----------
    in_list: List of length m
        the list in which exists the elements to be swapped as specified in index1 and index2 

    index1: int
        the index of the first element to be swapped.

    index2: int
        the index of the second element to be swapped.

    """

    in_list[index1], in_list[index2] = in_list[index2], in_list[index1] 

    return in_list


def main():
    in_list = [3, 6, 7, 8, 11, 4, 5, 1, 9]
    n = len(in_list)

    print(in_list)

    # sortlist = QuickSort(in_list)

    # testing length object
    print(f"the list length is: {len(in_list)}")

    # testing the swap method
    print('\ntesting the swap method')
    in_list = swap(in_list, 0, 2)
    print(in_list)

    in_list = swap(in_list, 0, n-1)
    print(in_list)

    in_list = swap(in_list, 3, 5)
    print(in_list)

    in_list = swap(in_list, 4, 5)
    print(in_list)

    # testing quicksort method
    print('\ntesting the quicksort method')
    in_list = quicksort(in_list, pivot_pick = 'first')
    print(in_list)

    in_list = quicksort(in_list, pivot_pick = 'last')
    print(in_list)

    in_list = quicksort(in_list, pivot_pick = 'median')
    print(in_list)

    # testing partition method
    print('\ntesting the partition method')
    in_list, _ = partition(in_list, 0, n-1)
    print(in_list)




if __name__ == "__main__": main()

"""SCRATCH

        # both indicies below begin at one because the 0-th element in the array is the pivot
        i = 1       # index between which the lists are going to be split along the pivot.
        j = 1       # the index that signifies what portion of the array has been searched over

        while j < self.length:
            
            
            j += 1      # increment j for the next pass of the loop

"""