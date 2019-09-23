""" Modulo para la validacion de datos

    Se proveen un conjuntode funciones, que tienen como objetivo
    la validacion de variables:
    - valInt: Enteros
    - valFloat: Flotantes
    - valComplex: Complejos
    - valList: Listas
"""

from math import sqrt
from utils import validate_range

_TYPE_ERROR = 'El rango indicado no es valido, debe ingresar una "list" o "tuple"'

def valInt(number, ran=None):
    """esta funcion recibe 1 parametro para saber si es entero o no, 
    tambien puede recibir dos parametros en los cuales el primero de estos indica el numero
    que se deasea buscar y el segundo el rango donde se desea buscar el numero, de encontrar
    el numero en el rango dado devuelve True"""
    if ran != None:
        if type(ran) not in (list, tuple):
            raise TypeError(_TYPE_ERROR)

        elif type(number) is not int:
            return False

        else:
            return validate_range(number, ran)

    if type(number) is int:
        return True
    else:
        return False

def valFloat(number, ran=None):
    """esta funcion recibe 1 parametro para saber si es flotante o no, 
    tambien puede recibir dos parametros en los cuales el primero de estos indica el numero
    que se deasea buscar y el segundo rango donde se desea buscar el numero, de encontrar
    el numero en el rango dado devuelve True"""
    if ran != None:
        if type(ran) not in (list, tuple):
            raise TypeError(_TYPE_ERROR)

        elif type(number) is not float:
            return False

        else:
            return validate_range(number, ran)

    if type(number) is float:
        return True
    else:
        return False

def valComplex(number, ran=None):
    """esta funcion recibe 1 parametro para saber si es complejo o no, 
    tambien puede recibir dos parametros en los cuales el primero de estos indica el numero
    que se deasea buscar y el segundo rango donde se desea buscar el numero, de encontrar
    el numero en el rango dado devuelve True, aqui bucara el modulo del numero complejo dado
    en el rango indicado"""
    if ran != None:
        if type(ran) not in (list, tuple):
            raise TypeError(_TYPE_ERROR)
    
        elif type(number) is not complex:
            return False

        else:
            mod = sqrt(number.real**2 + number.imag**2)
            return validate_range(mod, ran)

    if type(number) is complex:
        return True
    else: 
        return False

def valList(elements, to_compare=None, option=None):
    """Esta funcion recibe 1 o 3 argumentos, de ser uno solo, validara que el argumento sea
    una lista, al ser 3 el primero debe ser una lista, el segundo argumento puede ser un entero o una lista
    , esto viene definido por el tercer argumento que es un string, indicada si se desea, 
    comparar dos listas o si se desea validar la cantidad de elemntos en una lista, los valores que admite el
    string son 'values' o 'len'. No se admite el uso de solo dos argumentos para la funcion"""
    if option == 'values':
        if type(to_compare) is not list:
            raise TypeError('Debe ingresar una lista como segundo argumento si su opcion fue "values"')
        else:
            if elements == to_compare:
                return True
            else:
                return False

    elif option == 'len':
        if type(to_compare) is not int:
            raise TypeError('Debe ingresar un numero entero como segundo argumento si su opcion fue "len"')
        else:
            if len(elements) == to_compare:
                return True
            else:
                return False

    elif option != None:
        raise ValueError('La opcion ingresada no es correcta')
    
    elif option==None and to_compare != None:
        raise ValueError('Debe ingresar 1 o 3 argumentos')

    if type(elements) is list:
        return True
    else:
        return False

print(valInt(1, (1,6)))

print(valFloat(-55.0, (-55.1,103)))

print(valComplex(0j+1, [1,5]))

print(valList([1,2,1,1], 4, 'len' ))