import numpy as np
    
arr = np.array([10, 20, 30, 40])
indices = [2, 3]

print(arr[indices])   # [20 40]

mask = arr > 30
print(arr[mask])


print(np.sqrt(arr))
print(np.exp(arr))
print(np.add(arr,2))

print(arr)
arr_b=arr[1:3]
print(arr_b)
print(arr)

arr_b[0]=1

print(arr_b)
print(arr)
# print(arr_b)

arr_c = arr[1:3].copy()
print(arr_c)
print(arr)