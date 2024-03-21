def transpose_matrix(matrix):
    row, column = len(matrix), len(matrix[0])
    transposed = [[0] * row for _ in range(column)]

    for i in range(row):
        for j in range(column):
            transposed[j][i] = matrix[i][j]

    return transposed

if __name__ == "__main__":
    original_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transposed_matrix = transpose_matrix(original_matrix)

    print("From original matrix:")
    for row in original_matrix:
        print(row)

    print("The transposed matrix is:")
    for row in transposed_matrix:
        print(row)