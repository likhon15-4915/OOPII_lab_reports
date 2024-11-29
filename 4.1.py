def add_matrices(matrix1, matrix2):
 result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
 return result
