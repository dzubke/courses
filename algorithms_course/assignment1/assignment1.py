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

def single_digit multipy(int_1, int_2):
    '''Takes in two single-digit integers int_1 and int_2 and performs the multiplication algorithm taught in classrooms

    Parameters
    ----------
    int_1: integer
        the first integer to be multiplied

    int_2: integer
        the second integer to be multiplied

    Returns
    -----------

    product: integer
        the 
    
    carry: integer
        the carried integer in the multiplication

    '''
        #converting the integers into strings so we can iterate over them
        str_1 = str(int_1) 
        str_2 = str(int_2)

        product_list = []
        
        for i in range( len(str_1) ):
            product_list.append([])

            for j in range( len(str_2) ):

                 temp_prod (int( str_1[i] ) * int( str_2[j] ))

                 product_list[i].append( temp_prod % 10)
                 carry = 
