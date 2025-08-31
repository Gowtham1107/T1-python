import numpy as np

all_points = np.array([[1, 2], [3, 4], [5, 6]])        # Shape (3, 2)
central_point = np.array([[7, 8]])                   # Shape (1, 2)

diff = all_points - central_point
# print(diff)

print(diff**2)


# print(np.sum(all_points))

# print(np.sum(all_points, axis=0)) #columwise additon
# print(np.sum(all_points, axis=1)) #rowwise addition

distance=np.sqrt(np.sum(diff**2, axis=1))
print(distance)