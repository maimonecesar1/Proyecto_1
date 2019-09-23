"""En este modulo se definen funciones que son requeriadas por el modulo validation, 
debido a que eran procesos que se ejecutaban de manera repetitiva se decidio encapsular ese codigo en
funciones y colocarlas en un modulo a parte que luego seria requerido"""

def _number_in_range(number, init, end, is_tuple=False):
    """Funcion que evalua si un numero se encuentra en un rango dado, si el rango
    viene definido en una tupla no se tomara en cuenta los extremos, si es una lista 
    si seran tomados en cuanta"""
    if not is_tuple:
        return number >= init and number <= end
    else:
        return number > init and number < end

def _validateRange(number, ran):
    """Esta funcion valida que el rango intruducido cumpla con los parametros necesarios
    para que funcionen los metodos del modulo validate y a su vez ejecuta a la funcion
    _number_in_range y retorna su valor"""
    if len(ran) > 2 or len(ran) < 2:
        raise ValueError('El rango indicado no es correcto, se necesitan mas o menos datos para el rango')
    range_init = ran[0]
    range_end = ran[1]
    if range_init > range_end:
        raise ValueError('El rango indicado no es correcto')
    
    if type(ran) is list:
        return _number_in_range(number, range_init, range_end)

    elif type(ran) is tuple:
        return _number_in_range(number, range_init, range_end, is_tuple=True)      
    # else:
    #     return False 