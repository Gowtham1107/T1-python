def vector_add(A,B): 
    result=[]
    for i in range(len(A)):
        result.append(A[i]+B[i])
    return result

print(vector_add([1,2,3],[4,5,6]))


#using Numpy

import numpy as np

def np_vector_add(C,D):
    result = C+D
    return result
def np_vector_sub(C,D):
    result = C-D
    return result

C = np.array([1,2,3])
D = np.array([4,5,6])

print(np_vector_add(C,D))
print(np_vector_sub(C,D))


print(C+5)


#Broadcasting 

E = np.array([[1,2,3],[4,5,6]])
F = np.array([4,5,6])
print("broacasting")
print(np_vector_add(E,F))