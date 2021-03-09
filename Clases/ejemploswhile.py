#--Entradas---#
MENSAJE_BIENVENIDA = 'Muy buenos dias, despierte que estamos en clase de 6'
PREGUNTA_MENU = ''' Ingrese:
    1. Para mostrar los numeros del 1-5
    2. Para preguntar tu nombre
    3. Para mostrar el año en el que estamos
    4. Salir
 '''
PREGUNTA_NOMBRE = "Cual es su nombre?: "
MENSAJE_ERROR = 'Por favor ingrese un numero valido'
#---
entrada = 1
while (entrada >= 1 and entrada <=3):
    entrada = int (input(PREGUNTA_MENU))
    if (entrada == 1):
        print (1, 2, 3, 4)
    elif (entrada == 2):
        nombre = input (PREGUNTA_NOMBRE)
        print (f'Bienvenido {nombre} a este menu, emplea las opciones')
    elif (entrada == 3):
        print ('Estamos en el año 2021')
    elif (entrada == 4):
        print ('Muchas gracias por participar')
    else:
        entrada = 1
        print (MENSAJE_ERROR)

