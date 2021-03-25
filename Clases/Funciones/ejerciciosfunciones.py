#-------Sumar dos numeros------#
def sumar (a = 0, b = 0):   
    '''
        Devuelve la suma de dos numeros a y b, 
        por defecto ambos valen cero
    '''
    suma = a + b
    return suma

#-------Restar dos numeros------#

def restar (a = 0, b = 0):
    '''
        Devuelve la resta de un numero a con un numero b, 
        por defecto ambos valen cero
    '''
    resta = a - b
    return resta
#-------Multiplicar dos numeros------#

def multiplicar (a = 0, b = 0):
    '''
        Devuelve la multiplicacion de un numero a con un numero b, 
        por defecto ambos valen cero
    '''
    multiplicacion = a * b
    return multiplicacion
#-------Dividir dos numeros------#

def dividir (a = 0, b = 1):
    '''
        Devuelve la division de un numero a con un numero b, 
        por defecto a vale cero y b tiene valor de uno
    '''
    division = a / b
    return division
#-------Potenciar dos numeros------#

def potenciar (base = 0, exponente = 1):
    '''
        Devuelve la potenciacion de una base a con su exponente b, 
        por defecto la base vale 0 y el exponente tiene un valor de uno
    '''
    potencia = base ** exponente
    return potencia

#---Funciones dependientes de otas----#
def calcular (operacion, numeroA, numeroB):
    '''
        Permite escojer la operacion que se desea realizar,
        junto al calculo de esta operacion de un numero a y b
    '''
    print (operacion(numeroA,numeroB))

