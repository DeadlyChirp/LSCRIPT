def count_inner_smaller(matrix):
    # Counter for elements with all neighbors strictly smaller
    count = 0

    # Iterate over the matrix, avoiding the border elements
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            # Current element
            element = matrix[i][j]

            # Check if all four neighbors are strictly smaller
            if element > matrix[i - 1][j] and element > matrix[i + 1][j] and \
                    element > matrix[i][j - 1] and element > matrix[i][j + 1]:
                count += 1

    return count


# Test the function with the provided matrix
matrix = [[1, 4, 9, 1, 4], [4, 8, 1, 2, 5], [4, 1, 3, 4, 6], [5, 0, 4, 7, 6], [2, 4, 9, 1, 5]]
print(count_inner_smaller(matrix))
