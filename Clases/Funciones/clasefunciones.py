guardar = print ('Hola')
print (guardar)

guardar = round (14.234345, 2)
print (guardar)

def linedesign (cantidad = 10, patron = '.'):    #F(x,y) --> variables , =Patrones por defecto, cuando no hay nada en ()
    print (patron * cantidad)
    return None  

linedesign (30, '#')
linedesign (10, '*')
linedesign (10, 'ß')
linedesign()

#-----Muestre la lista ------#
def mostrarLista (listaEntrada):
    for elemento in listaEntrada:
        print (elemento)
        return None         #No devuelve algun valor, buena practica de programacion

lista = [12,435,78,32,65,321,657,434,67,23]
lista2 = [43,56,74,24,89,42,34,67,42,57,564]
linedesign (30, '#')
mostrarLista (lista)
linedesign (15, '-')
mostrarLista (lista2)
#-------Sumar dos numeros------#
def sumar (a = 0, b = 0):
    suma = a + b
    return suma
linedesign (30,'#')
resultado = sumar()
print (resultado)
print (sumar(12,14))
round (12.35443,2)

#-------Restar dos numeros------#
linedesign ()
def restar (a = 0, b = 0):
    resta = a - b
    return resta
#-------Multiplicar dos numeros------#
linedesign()
def multiplicar (a = 0, b = 0):
    multiplicacion = a * b
    return multiplicacion
#-------Dividir dos numeros------#
linedesign ()
def dividir (a = 0, b = 1):
    division = a / b
    return division
#-------Potenciar dos numeros------#
linedesign ()
def potenciar (base = 0, exponente = 1):
    potencia = base ** exponente
    return potencia

#---Funciones dependientes de otas----#
def calcular (operacion, numeroA, numeroB):
    print (operacion(numeroA,numeroB))


print(restar (83, 87))

print (multiplicar (83, 87))

print (dividir (83, 87))

print (dividir())

print (potenciar(5,6))

calcular (multiplicar, 63, 67)    

