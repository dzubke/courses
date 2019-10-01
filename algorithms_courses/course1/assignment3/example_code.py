# I got stuck in an infinite recusion and needed some help, so I drew some inspiration of the quicksortHelper function from this code. 
# I found this code at: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)


def quickSortHelper(alist,first,last):
   if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    print(f"first: {first}")
    print(f"last: {last}")

    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark

if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    quickSort(alist)
    print(alist)