# Understand the Matrix: A matrix in Python can be represented as a list of lists. Each sublist represents a row in the matrix.

# Accessing Neighbors: For a given element matrix[i][j], its neighbors are:

# Left: matrix[i][j-1]
# Right: matrix[i][j+1]
# Top: matrix[i-1][j]
# Bottom: matrix[i+1][j]
# Edge Cases: We need to ensure we don't try to access neighbors for the border elements since they don't have all four neighbors.
# So, we'll iterate from 1 to len(matrix)-2 for rows and 1 to len(matrix[0])-2 for columns.

# Comparison: For each element, check if all four neighbors are strictly smaller. If they are, increment a counter.

# Return the Result: After iterating through the entire matrix, return the counter value.


def voisinpluspetit(matrix):
    count = 0

    for i in range(len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            element = matrix[i][j]

            if element > matrix[i - 1][j] and element > matrix[i + 1][j] and element > matrix[i][j - 1] and element > \
                    matrix[i][j + 1]:
                count += 1

    return count


matrix = [[1, 4, 9, 1, 4], [4, 8, 1, 2, 5], [4, 1, 3, 4, 6], [5, 0, 4, 7, 6], [2, 4, 9, 1, 5]]
print(voisinpluspetit(matrix))
