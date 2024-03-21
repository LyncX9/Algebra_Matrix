def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for j in range(n):
            submatrix = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]
            sign = (-1) ** j
            determinant += sign * matrix[0][j] * det(submatrix)
        return determinant

if __name__ == "__main__":
    matrix = [
        [4, 7, 2],
        [2, 6, 1],
        [3, 5, 9]
    ]
    result = det(matrix)
    print("Determinant of the matrix is:", result)
