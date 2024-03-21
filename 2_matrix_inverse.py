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

def adjoint(matrix):
    n = len(matrix)
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            submatrix = [[matrix[k][l] for l in range(n) if l != j] for k in range(n) if k != i]
            sign = (-1) ** (i + j)
            adj[j][i] = sign * det(submatrix)
    return adj

def inverse(matrix):
    determinant = det(matrix)
    if determinant == 0:
        raise ValueError("Matrix is not invertible.")
    adj = adjoint(matrix)
    inverse_matrix = [[adj[i][j] / determinant for j in range(len(adj))] for i in range(len(adj))]
    return inverse_matrix

if __name__ == "__main__":
    matrix = [
        [4, 7, 2],
        [2, 6, 1],
        [3, 5, 9]
    ]
    result = inverse(matrix)
    print("Inverse of the matrix is:")
    for row in result:
        print(row)