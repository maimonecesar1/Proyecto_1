"""Modulo para controlar errores comunes en el modulo de algebra"""

def error_compatibility(matrix_a, matrix_b):
    """Valida que las dimensiones sean compatibles para realizar multiplicacion de matrices"""
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError('Las dimensiones de las matrices no son compatibles.')
    
    pass

def error_tam_lists(matrix):
    """valida que las listas que representan la filas de la matriz contengan la misma cantidad de elemntos"""
    tam = len(matrix[0])
    for i in matrix:
        if tam != len(i):
            raise ValueError('La matriz debe tener el mismo numero de elementos en cada lista')

    pass

def error_simmetry(matrix):
    """valida que lamatriz sea cuadrada"""
    if len(matrix) != len(matrix[0]):
        raise ValueError('La matriz debe ser cuadrada para poder ejecutar esta funcion')

    pass