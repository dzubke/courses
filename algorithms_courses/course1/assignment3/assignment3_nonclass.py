# assignment3_nonclass.py
# this was the first code to run successfully, but I wanted to implement quicksort with a class object as in assignment3.py
# effecitively this was supporting code. A more verbose version of this code can be found in assignment3_scratch.py which I used for debugging purposes

# standard libraries
from typing import List, Tuple
from statistics import median
from math import floor


def quicksort(in_list: List, pivot_pick: str ='first') -> None:
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

    """
    n = len(in_list)                    # lenght of input lists

    comparison_total = quicksortHelper(in_list, 0, n, pivot_pick = pivot_pick)

    return comparison_total


def quicksortHelper(in_list, l_index, r_index, pivot_pick = 'first'):
    """A helper function for quicksort in which the resursive calls will be made.
    """

    comparison_count = 0
    count_left = 0 
    count_right = 0
    
    if l_index < r_index: 

        if pivot_pick == 'first':       # if the pivot picking method is 'first'
            pass                        # then set the pivot as the first element

        elif pivot_pick == 'last':          # if the pivot memthod is 'last'
            in_list = swap(in_list, l_index, r_index-1)            # then set the pivot as the last element

        elif pivot_pick =='median':                            # if the pivot choosing method is 'median-of-three'
            # the pivot will be the median of the first, middle, and last elements
            median_index_org = floor( (r_index - 1 + l_index) /2)        # this calculates the index of the median element in the original list
            median_pivot = median([in_list[l_index], in_list[ median_index_org ], in_list[ r_index-1 ] ] ) 

            # then swap whichever value was picked as the median-of-three with the first value in the array
            if median_pivot == in_list[l_index]:
                pass        # don't do anything because the median is already in the l_index position

            elif median_pivot == in_list[ median_index_org ]:       # if the median in the original list was picked
                in_list = swap(in_list, l_index, median_index_org)  # swap it with the first element

            elif median_pivot == in_list[ r_index-1 ]:              # if the last element of the list was picked
                in_list = swap(in_list, l_index, r_index - 1 )      # swap it with the first element

        else:   # if pivot_pick is not equal to 'first', 'last', or 'median-of-three' raise the ValueError
            raise ValueError("invalid entry for pivot_pick argument. Valid entries are 1) 'first', 2) 'last', or 3) 'median'")

        pivot_index = partition(in_list, l_index, r_index)
        comparison_count = r_index - l_index - 1

        count_left = quicksortHelper(in_list, l_index, pivot_index, pivot_pick=pivot_pick)
        count_right = quicksortHelper(in_list, pivot_index+1, r_index, pivot_pick=pivot_pick)

    comparison_total = comparison_count + count_left + count_right       # the number of comparisons done by the call of the quicksort algorithm

    return comparison_total



def partition(in_list, l_index: int, r_index: int) -> int:
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

    i = l_index + 1              # the i-th index that separates values less than (<i) and greater (>i) of the pivot

    # print(f"i and r_index are: {i, r_index}")

    for j in range(i, r_index):
        
        if in_list[j] < pivot:     # if the j-th element is less than the pivot 
            in_list = swap(in_list, i, j)          # swap the i-th element with the j-th element since i is boundary index and the i-th element is greater than the pivot
            i += 1                   # increment i
            # print("increment i")

    in_list = swap(in_list, l_index, i-1)   #after the loop has sorted the array, swap with pivot into place

    return i-1      # returns the index of the pivot for use in the quicksort recursion


    
def swap(in_list: List, index1: int, index2: int) -> List:
    """This method will swap the elements in index1 and index2.
       
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
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(in_list)

    count_first = quicksort(in_list, pivot_pick='first')
    count_last = quicksort(in_list, pivot_pick='last')
    count_median = quicksort(in_list, pivot_pick='median')

    print(in_list)
    print(count_first)
    print(count_last)
    print(count_median)

    count_first_sort = quicksort(sorted_list, pivot_pick='last')
    print(count_first_sort)
    
    with open('data_QuickSort.txt', 'r') as f:
        data_list_first = [int(line.strip()) for line in f]
    
        print(data_list_first[:15])
        print(f"data list len: {len(data_list_first)}")

        data_count_first = quicksort(data_list_first, pivot_pick='first')
        print(data_list_first[:15])
        print(f"the first count is: {data_count_first}")

        assert data_list_first  == [x for x in range(1, 10001)]
        assert data_count_first == 162085
    

    with open('data_QuickSort.txt', 'r') as f:
        data_list_last = [int(line.strip()) for line in f]
    
        print(data_list_last[:15])
        print(f"data last len: {len(data_list_last)}")

        data_count_last = quicksort(data_list_last, pivot_pick='last')
        print(data_list_last[:15])
        print(f"the last count is: {data_count_last}")

        assert data_list_last  == [x for x in range(1, 10001)]
        assert data_count_last == 164123


    with open('data_QuickSort.txt', 'r') as f:
        data_list_median = [int(line.strip()) for line in f]
    
        print(data_list_median[:15])
        print(f"data median len: {len(data_list_median)}")

        data_count_median = quicksort(data_list_median, pivot_pick='median')
        print(data_list_median[:15])
        print(f"the median count is: {data_count_median}")
        
        assert data_list_median  == [x for x in range(1, 10001)]
        assert data_count_median == 138382


    #data_count_last= quicksort(data_list_last, pivot_pick='last')
    #data_count_median = quicksort(data_list_first, pivot_pick='median')

    
    # print(f"the last count is: {data_count_last}")
    # print(f"the median count is: {data_count_median}")
 

    



if __name__ == "__main__": main()
