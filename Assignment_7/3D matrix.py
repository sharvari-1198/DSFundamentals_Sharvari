# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:59:30 2024

@author: Sharvari
"""

#finds and returns the longest contiguous sequence of 1s in any horizontal slice of the matrix, 
#along with the starting position of this sequence.

import numpy as np

def generate_matrix(x, y, z):        #generate 3d matrix with indices x,y,z
    matrix = np.zeros((x, y, z), dtype=int)
    
    for i in range(x):
        for j in range(y):
            for k in range(z):
                sum = i + j + k
                if (sum % 10 == 0) or (sum % 100 == 2):
                    matrix[i, j, k] = 0  # Even sum of indices
                else:
                    matrix[i, j, k] = 1  # Odd sum of indices
    
    return matrix

def longest_substring(matrix):
    x, y, z = matrix.shape
    max_length = 0
    max_position = None
    
    for i in range(x):
        for j in range(y):
            current_length = 0
            for k in range(z):
                if matrix[i, j, k] == 1:
                    current_length += 1
                    if current_length > max_length:
                        max_length = current_length
                        max_position = (i, j, k - current_length + 1)
                else:
                    current_length = 0
    
    return max_length, max_position

# Example usage:
x_dim, y_dim, z_dim = 7, 5, 3
# Generate the 3D matrix
matrix = generate_matrix(x_dim, y_dim, z_dim)

# Output the matrix
for i in range(x_dim):
    for j in range(y_dim):
        for k in range(z_dim):
            print(f"matrix[{i}][{j}][{k}] = {matrix[i][j][k]}")
        print()
    print()

#longest_length, start_position = longest_substring(matrix)
longest_length, start_position, coordinates = longest_substring(matrix)
print(f"Longest substring of 1s length: {longest_length}")
print(f"Starting position of longest substring: {start_position}")
print("Coordinates of longest substring:")
for coord in coordinates:
    print(coord)
