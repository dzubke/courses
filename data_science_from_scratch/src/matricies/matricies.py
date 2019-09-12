# There are a few simple implementations of list comprehensions in building up vector and matrix operations that I want to try. 
# It is still a little difficult to read code and fully understand it, so these little recreations will help. 
# Again, this code is taken from the book Data Science from Scratch by Joel Grus. 


from typing import List

#type alias for Vector
Vector = List[float]
#type alias for Matrix
Matrix = List[List[float]]


def vector_sum(vectors: List[Vector]) -> Vector: 
    """Sums all corresponding elements in a list of vectors"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check that vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the i-th elemtn of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]



def my_vector_sum(vectors: List[Vector]) -> Vector:
    """I didn't fully understand what the return statement of vector_sum was doing. The code below is how I would have written it.
        The vector_sum is much more concise. 
    """
    num_elements: int = len(vectors[0])
    vec: Vector = []

    for i in range(num_elements): 
        temp_val: float = 0
        for vector in vectors: 
            temp_val += vector[i] 
        vec.append(temp_val) 
    
    return vec

#Again, the use of list comprehensions in the return statement of the get_row function below is a bit confusing to me.
def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j]          #jth element of row A_i
            for A_i in A]   #for each row A_i

#The return statment is able to run the generator from the for-loop and put each call of the generator into the list


from typing import Callable
#this function will be used in the identity_matrix function below. I want to better understand the use of the Callable object
def make_matrix(num_rows: int, 
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix whose (i,j)-th entry is entry_fn(i,j)
    """
    return [[entry_fn(i,j)              # given i, create a list
            for j in range(num_cols)]   # [entry_fn(i,0), ....]
            for i in range(num_rows)]   # create one list for each i

def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix (3) ==  [[1, 0, 0],
                                [0, 1, 0],
                                [0, 0, 1]]

if __name__ == "__main__":
    
    vectors = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    assert vector_sum([[1,2], [3,4], [5,6], [7,8]]) == [16,20]
    assert my_vector_sum([[1,2], [3,4], [5,6], [7,8]]) == [16,20]

    assert get_column(vectors, 0) == [1, 4, 7]

    #playing with the lambda expression
    x = lambda y: y + 1
    assert x(2) == 3

    #the use of the lambda expression with the if-else statement is what was most confusing. I think I get it now.
    z = lambda m: m + 1 if m==1 else 0
    assert z(1) == 2
    assert z(5) == 0
