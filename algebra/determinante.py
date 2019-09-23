"""
Modulo para calculo de determinante

por ser una funcion extra se decidio colocar a parte de las
demas funciones del modulo de algebra, en este modulo por medio de la
recurrencia de funciones se calcula el determinante de una matriz
"""

from utils import null_matrix

def determinant(matrix):
    """duncion para el calculo del determinante

        Recibe un unico parametro que debe ser una lista de listas y calula el 
        determinante de esa matriz
    """
    order = len(matrix)
    det = 0
    if order == 1:
        det = matrix[0][0]
    else:
        for j in range(order):
            det = det + matrix[0][j] * cofactor(matrix, 0, j)
    # import pdb; pdb.set_trace()
    return det

def cofactor(matrix, row, colunm):
    """ Funcion para calcular los cofactores

        Recibe la matriz con que se trebaja en el momento y las posiciones de las filas y columnas 
        que no seran requeridas para la nueva submatriz. Es aqui donde ocurre la recurrencia ya que
        esta funcion invoca a la funcion determinant() que a su vez llama a cofactor()
    """
    order = len(matrix)
    ran = order - 1
    x, y = 0, 0
    submatrix = null_matrix(ran, ran)

    for i in range(order):
        for j in range(order):
            if(i != row and j != colunm):
                submatrix[x][y] = matrix[i][j]
                y = y + 1
                if y >= ran:
                    x = x + 1
                    y = 0

    # import pdb; pdb.set_trace()
    a = determinant(submatrix)
    b = (-1)**(row+colunm)
    return a*b

matrix = [[1,2,3], [0,4,5], [0,0,7]]
matrix2 = [[3,2,-3], [7,-1,0], [2,-4,5]]
# matrix3 = [[3, 2, -3, 4, 5], [7, -1, 0, 6, 7], [ 2, -4, 5, 2, 3], [1, 3, 4, 5, -10], [-3, 4, 12, -15, 6]]

# print(determinant(matrix))