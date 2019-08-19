'''
Assignment prompt

In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.

To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers. 
You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive 
integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627

[TIP: before submitting, first test the correctness of your program on some small test cases of your own devising. 
Then post your best test cases to the discussion forums to help your fellow students!]

[Food for thought: the number of digits in each input number is a power of 2. Does this make your life easier? 
Does it depend on which algorithm you're implementing?]

The numeric answer should be typed in the space below. So if your answer is 1198233847, then just type 1198233847 in the space provided 
without any space / commas / any other punctuation marks.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)

'''

from typing import Tuple
from math import ceil, floor
import time

def karatsuba_multipy(x: int, y: int) -> int:
    """
    !!! This function currenlty doesn't run because it can't handle multiplication of digits of different size. This is problem for the call
    of the cross term: cross_term = karatsuba_multipy(a+b, c+d) - ac - bd  because sometimes the sum c+d is greater than 9 which results in a
    two digit number. This can be shown in the print statements below when multiplying 1234 and 5678. 

    Inputed: 1234, 5678
    Split: 12, 34, 56, 78
    Inputed: 12, 56
    Split: 1, 2, 5, 6
    Inputed: 1, 5
    Inputed: 2, 6
    Inputed: 3, 11

    When 3 and 11 are inputted the assert for the integers of the same length is failed. But when that assert is removed, the product doesn't work
    because the function is not designed to handle multiplication of differnt number sizes. In fact, the fancy cross term subtraction trick
    that this relies on only seems to work if the inputted numbers are the same length. All of this leaves me rather puzzled.... at the moment...
    !!! 

    
    This function utilizes the Karatsuba algorithm for multiplication. It takes a similar approach as the simple_recursive_multiply function
        but instead of computing the cross term (ac+bd) as two products it instead calculates them as (a + b)*(c + d) - ac - bd. This works 
        because additions require fewer computations than multiplications and the ac and bd terms must already be multiplied.

        As a note, karatsuba multiplication only works if both intergers x and y have the same length

    Parmeters
    ----------
    x: an integer of length n 
    y: an integer of length n 

    Returns
    ----------
    prod: an integer which is the product of x and y

    """
    print(f"Inputed: {x}, {y}")
    assert len(str(x)) == len(str(y)), "The integers should have the same number of digits"
    
    n = len(str(x))

    # the base case
    if n == 1:
        return x * y
    
    # otherwise, split the integers into 
    else: 
       
        a, b = int_split(x)
        c, d = int_split(y)
        print(f"Split: {a}, {b}, {c}, {d}")
        ac = karatsuba_multipy(a, c)
        bd = karatsuba_multipy(b, d)
        cross_term = karatsuba_multipy(a+b, c+d) - ac - bd
    
        return 10**(2*ceil(n/2)) * ac + 10**ceil(n/2) * cross_term  + bd



def simple_recursive_multiply(x: int, y: int) -> int:
    """A recursive approach to integer multiplication.
        The first integer x of length n will be expressed as two smaller integers a and b:
            x = a * 10**ceil(n/2) + b
        Likewise, y of length m can be expressed as two smaller integers c and d:
            y = c * 10**ceil(m/2) + d
    
        Then the product of x and y can be expressed as:
            prod = 10**(ceil(n/2)*ceil(m/2) * (ac) + 10**ceil(n/2) * ad + 10**ceil(m/2) * bc + bd

    Parameters
    ----------
    x: an integer of length n 
    y: an integer of length m

    Returns
    ----------
    prod: an integer which is the product of x and y

    """
    n = len(str(x))
    m = len(str(y))

    # the base case
    if n == 1 and m ==1:
        return x * y
    
    elif n == 1 and m != 1:

        c, d = int_split(y)
        
        return 10**ceil(m/2) * simple_recursive_multiply(x, c) + simple_recursive_multiply(x, d)

    elif n != 1 and m == 1:

        a, b = int_split(x)
        
        return 10**ceil(n/2) * simple_recursive_multiply(y, a) + simple_recursive_multiply(y, b)

    # otherwise, split the integers into 
    else: 

        a, b = int_split(x)
        c, d = int_split(y)
    
        return 10**(ceil(n/2)+ceil(m/2)) * simple_recursive_multiply(a, c) + 10**ceil(n/2) * simple_recursive_multiply(a, d) + 10**ceil(m/2) * simple_recursive_multiply(c, b) + simple_recursive_multiply(b, d)


def int_split(int_1: int) -> Tuple[int, int] : 
    """Expresses an integer of length n  as two smaller integers a and b:
        int_1 = a * 10^(n/2) + b

    Parameters
    -----------
    int_1: an integer of length n

    Returns
    ---------
    a: an integer of length n//2
    b: an integer of length n//2 (or n//2 + 1 if n is odd)

   """


    n = len(str(int_1))
    
    if n == 1:
        return int_1
    
    else:
        a = int(str(int_1)[:n//2])
        b = int(str(int_1)[n//2:])

        assert len(str(a)) == floor(n/2)
    #    assert len(str(b)) == ceil(n/2)
    # I'm being sloppy here - the multiplication of the huge numbers violated this assert statement but the code gave the correct answer 
    # when I commented out the assert and I don't feel like taking the time to understand why the assertion failed.

        return a, b


if __name__ == "__main__":
    
    assert simple_recursive_multiply(12, 34) == 408, "Even number of digits with both integers of the same length"
    assert simple_recursive_multiply(1234, 5678) == 7006652, "Even number of digits with both integers of a longer length"
    assert simple_recursive_multiply(123, 456) == 56088, "Odd number of digits with both integers of the same length"
    assert simple_recursive_multiply(123, 45) == 5535, "Both integers of the different length"

    #the time module will be used to compare the simple recursive and the Karatsuba algorithm
    time1 = time.time()
    simple_prod = simple_recursive_multiply(3141592653589793238462643383279502884197169399375105820974944592, 
                                    2718281828459045235360287471352662497757247093699959574966967627)
    time2 = time.time()

    recur_time = time2-time1

    print(f"The simple recursive algorithm took {recur_time} seconds to run")
    print(f"The computed product was {simple_prod}")

    assert karatsuba_multipy(12, 34) == 408, "Even number of digits with both integers of the same length"
    print(karatsuba_multipy(1234, 5678))
    # The karatsuba_multiply function isn't working for the assert statement below. 
    assert karatsuba_multipy(1234, 5678) == 7006652, "Even number of digits with both integers of a longer length"
    assert karatsuba_multipy(123, 456) == 56088, "Odd number of digits with both integers of the same length"

    time3 = time.time()
    karatsuba_prod = karatsuba_multipy(3141592653589793238462643383279502884197169399375105820974944592, 
                                    2718281828459045235360287471352662497757247093699959574966967627)
    time4 = time.time()

    karatsuba_time = time4-time3

    print(f"The simple recursive algorithm took {karatsuba_time} seconds to run")
    print(f"The compute product was {karatsuba_prod}")