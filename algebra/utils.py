def one_search(matrix, tam, i, identity):
    """busca o crea un 1 para la diagonal principal, ya sea por intercambio de filas
    o division de la fila"""
    if matrix[i][i] != 1:
        if matrix[i][i] == 0:
            rotate_row(i, matrix, identity)

        div = matrix[i][i]        
        for j in range(tam):
            matrix[i][j] = matrix[i][j] / div
            identity[i][j] = identity[i][j] / div

    return matrix, identity

def rotate_row(i, matrix, identity):
    rotate =  False
    for x in range(i+1, len(matrix)):
        if matrix[x][i] != 0:
            matrix[i], matrix[x] = matrix[x], matrix[i]
            identity[i], identity[x] = identity[x], identity[i]
            rotate = True
            break 
        else:
            continue
    
    if rotate:
        return matrix, identity
    else:
        raise ZeroDivisionError('La matriz no posee inversa')

def zero_search(matrix, i, j, tam, identity):
    """busca o crea un 0, por resta de la filas"""
    if matrix[i][j] != 0:
        val = matrix[i][j]
        for z in range(tam):
            matrix[i][z] = matrix[i][z] - (matrix[j][z]*val)  
            identity[i][z] = identity[i][z] - (identity[j][z]*val)  
            #import pdb; pdb.set_trace()
   
    return matrix, identity

def identity_generate(tam):
    """crea una matriz identidad segun el tamano que se le indique"""
    indentity = null_matrix(tam, tam)

    for i in range(tam):
        indentity[i][i] = 1
    return indentity

def null_matrix(rows, columns):
    """cra una matriz nula segun el tamano que se le indique"""
    matrix = []
    for i in range(rows):
        matrix.append([0]*columns)

    return matrix

