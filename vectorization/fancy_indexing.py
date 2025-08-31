import numpy as np

a = np.array([1, 2, 3, 4])

print(a[[1,3]])

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12],
                   [11, 22, 1, 2]])

print(matrix[[1,2]])
print(matrix[1, 1:3])

print(matrix[1:, 1:3])

print(matrix[1:, 1])

print(matrix[2:, :3])


matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12]])

print(matrix[[1,2], [2,3]])


print("np.ix")

grades = np.array([[85, 92, 78, 88],  # Alice*
                   [76, 84, 90, 82],  # Bob
                   [95, 89, 85, 91]]) #Charlie

a = [0,2]
b = [0,2]
print(grades[np.ix_(a,b)])

c=[1,2]
d=[1,3]
print(grades[np.ix_(c,d)])

grades[np.ix_(c,d)] = 0

print(grades)