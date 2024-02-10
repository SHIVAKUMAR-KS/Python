import numpy as np

# Create a 2D NumPy array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Find maximum element in each column
max_in_columns = np.max(matrix, axis=0)

# Find minimum element in each row
min_in_rows = np.min(matrix, axis=1)

# Find sum of elements in each row
sum_of_rows = np.sum(matrix, axis=1)

# Print the results
print("Maximum element in each column:", max_in_columns)
print("Minimum element in each row:", min_in_rows)
print("Sum of elements in each row:", sum_of_rows)
