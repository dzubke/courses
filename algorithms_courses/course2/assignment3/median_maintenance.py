# heap.py

# standard python libraries
from typing import List
import heapq as hq
from dataclasses import dataclass


@dataclass
class MedianMaintenance():
    """This algorithm will solve the median maintenance where a series of n numbers are given and this algorith must return the median of the numbers in log(n) time
    to achieve this, a heap data structure will be used. First, I will code up the algorithm using python's built-in heapq data structure
    and then I will attempt to implement a heap data structure from scratch.

    Parameters
    ----------
    heap_high: List[int]
        all numbers in heap_high are greater than those in heap_low. the minimum value of heap_high will be used to understand where to input new values given
        and also how to returnt the median


    """
    heap_high: List[int] = []        
    heap_low: List[int]  = []       # the values in heap_low are stored as negative of their input value since heapq returns the min values, and want to return the max of heap_min


    def new_number(self):
        """this function will handle adding a new number to either heap_high or heap_low

        """

    def return_median(self):
        """this function will return the median of the inputted numbers

        """


def main():
    """this function will input the data and call the methods in MedianMaintenance to return

    """
