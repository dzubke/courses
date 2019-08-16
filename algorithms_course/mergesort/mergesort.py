#This code implements the merge sort algorithm. It was made in conjunction with the Stanford Algorithm's course on Coursera
#Much of this code comes from Amir Zai's medium article on the merge sort algorithm - https://medium.com/@amirziai/merge-sort-walkthrough-with-code-in-python-e4f76d90a4ea


def split(in_list):
    '''Split a list in to two pieces
    
    Parameters
    ----------
    in_list: list of abitrary length n
        the inputted list to be split

    Returns
    ----------
    left_list: list of length n/2
        the left side of in_list
    
    right_list: list of length n/2 (or n/2 +1 if n is odd)
        the right side of in_list

    '''

    mid = len(in_list) // 2
    left_list = in_list[:mid]
    right_list = in_list[mid:]

    return left_list, right_list


def merge_sorted_list(left_list, right_list):
    '''Combines two sorted lists left_list and right_list together to return a single sorted list

    Parameters
    ----------
    left_list: list of length n where n is non-negative
        a list of integers arranged in ascending order
    
    right_list: list of length m where m is non-negative
        a list of integers arranged in ascending oder

    Return
    ----------
    merged_list: list of length n+m 
        a list combining left_list and right_list arranged in ascending order

    '''

    #Special case: one or both of the lists are empty
    if len(left_list) == 0:
        return right_list
    elif len(right_list) == 0:
        return left_list
    
    #General case: comparing left_list and right_list element-wise with pointers progressing through each element of the lists

    left_index = right_index = 0    #the points of the left_list and right_list
    merged_list = []    #the final, single list to be returned
    merged_list_target_len = len(left_list) + len(right_list)   #the final length of merged_list (n + m)

    while len(merged_list) <= merged_list_target_len:
        if left_list[left_index] <= right_list[right_index] :
            merged_list.append(left_list[left_index])
            left_index += 1
        else:
            merged_list.append(right_list[right_index])
            right_index += 1
        
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
    
    return merged_list


def merge_sort(in_list):
    '''Combining the split and merge_sorted_list function together to perform merge sort algorithm

    Parameters
    -----------
    in_list: list of length m


    Returns
    ----------


    '''

    if len(in_list) <= 1:
        return in_list
   
    else:
        left, right = split(in_list)
    
    
    return merge_sorted_list( merge_sort(left), merge_sort(right) )
    




if __name__ == '__main__':

    #I'll run a few tests to verify each funciton is doing what I think it should
    

    #testing the split function
    #list of odd length
    split_test_in_list_1 = [1, 2, 3]
    split_test_out_lists_1 = split(split_test_in_list_1)
    #list of even length
    test_list_2 = [1, 2, 3, 4]
    split_lists_2 = split(test_list_2)
    #list of single value
    test_list_3 = [1]
    split_lists_3 = split(test_list_3)
    #list with no values
    test_list_4 = []
    split_lists_4 = split(test_list_4)
    print('Testing the split function')
    print(f'Testing list of odd length: {split_test_in_list_1} split into {split_test_out_lists_1}' )
    print(f'Testing list of even length: {test_list_2} split into {split_lists_2}' )
    print(f'Testing list of one element: {test_list_3} split into {split_lists_3}' )
    print(f'Testing empty list: {test_list_4} split into {split_lists_4}' )
    print('')


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