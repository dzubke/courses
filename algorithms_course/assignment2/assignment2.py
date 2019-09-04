"""
Assignment #2 Prompt
--------------------

This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the i-th row of the file indicates the i-th entry of an array.

Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising. Then post your best test cases to the discussion forums to help your fellow students!]

"""

# standard libraries
from typing import List, Tuple

def sort_count(int_list: List[int]) -> Tuple[List[int], int]: 
    """ This function utilizes a divide-and-conquer recursive algorithm to count the number of inversions in an input list. 
        An inversion occurs when two number should be swapped to result in a sorted list increasing from left to right

    Parameters
    ----------
    int_list: list of integers with length n
        the list of integers is unsorted.

    Returns
    ----------
    inversion_count: int
        a count of the number of inversions in the int_list input
    """

    # checks that the inputs are the correct type
    assert type(int_list) == list, "input is not a list"

    # length of the list
    n  = len(int_list)

    # base case
    if n <= 1:
        return int_list, 0
    
    else: 
        # calculates the midpoint of the list
        midpt = n // 2

        # recursive call that counts the inversions in the left half of the list
        left = int_list[:midpt]
        right = int_list[midpt:]
        # print(f"sort_count right: {right}")       # debugging code

        # recursive call that counts the number of split inversions 
        
        return merge_count( sort_count(left), sort_count(right) )


def merge_count(left_output: Tuple[List[int], int], right_output: Tuple[List[int], int] ) -> Tuple[List[int], int]: 
    '''Merges two sorted lists left_list and right_list and counts the number of split inversions between the two

    Parameters
    ----------
    left_list: list of length n 
        a list of integers arranged in ascending order
    
    right_list: list of length m where m is non-negative
        a list of integers arranged in ascending oder

    Return
    ----------
    merged_list: list of length n+m 
        a list combining left_list and right_list arranged in ascending order

    '''
    
    # checks that the inputs are the correct type
    assert type(left_output) == tuple, "input is not a tuple"
    assert type(right_output) == tuple, "input is not a tuple"


    # unpack the output from the previous calls of merge_count
    left_list, left_count = left_output
    right_list, right_count = right_output


    #Special case: one or both of the lists are empty
    if len(left_list) == 0:
        return right_list, 0
    elif len(right_list) == 0:
        return left_list, 0
    
    #General case: comparing left_list and right_list element-wise with pointers progressing through each element of the lists

    left_index = right_index = 0    #the points of the left_list and right_list
    merged_list: List[int] = []    #the final, single list to be returned
    merged_list_target_len: int = len(left_list) + len(right_list)   #the final length of merged_list (n + m)
    inversion_count: int = left_count + right_count    # the count of the number of inversions

    while len(merged_list) <= merged_list_target_len:
        # print(f"right list value: {right_list}")      # debugging code
        if left_list[left_index] <= right_list[right_index] :
            merged_list.append(left_list[left_index])
            left_index += 1
        else:
            merged_list.append(right_list[right_index])
            right_index += 1
            inversion_count += len(left_list) - left_index  # counts the nubmer 
        
        #if we are at the end of the list, we can take a shortcut
        if right_index == len(right_list):
            # Reached the end of the right list
            # Append the remainder of the left list and break
            merged_list.extend(left_list[left_index:])
            break
        
        elif left_index == len(left_list):
            # Reached the end of the left list
            # Append the remainder of the right list and break
            merged_list.extend(right_list[right_index:])
            break
    
    return merged_list, inversion_count


def txt_to_list(txt_fn: str) -> List[int] : 
    """This function takes in a txt filename and reads the contents of the file (100,000 integers) into a list

    Parameters
    ----------
    txt_fn: str
        a string pathname to the file IntegerArray.txt

    out_list: List[int]
        a list of the 100,000 integers in the IntegerArray.txt file
    """

    with open(txt_fn, 'r') as f:
        out_list = [int(line.strip()) for line in f]

    return out_list

if __name__ == "__main__":

    int_list = txt_to_list('IntegerArray.txt')

    print(int_list[:15])

    merged_list_2, count_2 = sort_count(int_list)

    print(count_2)

