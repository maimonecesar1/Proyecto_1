"""Modulo para calculos con matrices por medio de diferntes funciones 
del algebra, producto matricial, matriz inversa, producto vectorial,
trasposicion de matrices y sistemas de ecuaciones"""

from utils import one_search, zero_search, identity_generate, null_matrix
from errors_controller import error_compatibility, error_simmetry, error_tam_lists
from determinante import determinant

def matrix_product(matrix_a, matrix_b):
    """Calculo del preoducto de dos matrices
        
        Recibe dos listas de listas como parametros para realizar los calculos 
        necesarios para el producto matricial
    """
    error_compatibility(matrix_a, matrix_b)
    error_tam_lists(matrix_a)
    error_tam_lists(matrix_b) 

    rows_a = len(matrix_a)
    columns_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    columns_b = len(matrix_b[0])

    new_matrix= null_matrix(rows_a, columns_b)
    for i in range(rows_a):
        for j in range(columns_b):
            for z in range(columns_a):
                new_matrix[i][j] += matrix_a[i][z] * matrix_b[z][j]

    return new_matrix

def inverse_matrix(matrix):
    """Calculo de la inversa de una matriz

        Recibe como parametro una lista de listas que representa una matriz
        y si la funcion tiene inversa la retorna. De lo contraria informa que hubo error
        o que no tenia inversa la matriz ingresada
    """
    error_tam_lists(matrix)
    error_simmetry(matrix)

    order = len(matrix)
    identity = identity_generate(order)
    for j in range(order):
        one_search(matrix, order, j, identity)
        for i in range(order):
            if i != j:
                zero_search(matrix, i, j, order, identity)    

            else:
                continue
    inverse = identity
    return inverse

def vectorial_product(v_a, v_b):
    """Producto vectorial

        recive dos listas con los componentes de cada vector
        y crea las matrices respectivas de cada elemento para calcular el determinante simbolico
        correspondiente a cada componente del nuevo vector, que es retornado como un diccionario
        """
    i_matrix = [ [v_a[1], v_a[2]] ,  [v_b[1], v_b[2]] ]
    j_matrix = [ [v_a[0], v_a[2]] ,  [v_b[0], v_b[2]] ]
    k_matrix = [ [v_a[0], v_a[1]] ,  [v_b[0], v_b[1]] ]

    new_vector = {
        'i': determinant(i_matrix),
        'j': -determinant(j_matrix),
        'k': determinant(k_matrix),
    }
    
    return new_vector

def trasposition(matrix):
    """Trasposicion de matrices

        Funcion para transponer matrices 
        """

    error_tam_lists(matrix)
    tam_rows, tam_colunms = len(matrix[0]), len(matrix)
    matrix_trans = null_matrix(tam_rows, tam_colunms)
    
    for i in range(tam_colunms):
        for j in range(tam_rows):
            matrix_trans[j][i] = matrix[i][j]

    return matrix_trans

def ecuations_sistem(coeficents, independent_terms):
    """Calculo de un sistema de ecuaciones

        Utilizando el metodo de la matriz inversa para el calculo de un sistema de ecuaciones,
        esta funcion hace uso de la funcion de inversion y de producto matricial para calcular
        sistemas de ecuaciones"""

    independent_matrix = [[x,] for x in independent_terms]
    invers = inverse_matrix(coeficents)
    solution = matrix_product(invers, independent_matrix)
    
    return solution

