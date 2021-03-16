#1. Escribir un programa que muestre la sumatoria de todos los números entre el 0 y el 100
sumatoria = 0
for suma in range (101):
    sumatoria += suma
print (sumatoria)

#2. Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
pregunta_factorial = 'Ingresa el numero al que le quieras sacar el factorial: '
factorial = 1
ingresar_factorial = int(input(pregunta_factorial))
for i in range (ingresar_factorial):
    factorial = factorial * (i+1)
print (factorial)

#3. Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
#No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.

sumaPositivos = 0
sumaNegativos = 0
cantidadPositivos = 0
for i in range (6):
    numero = int (input ('Numero: '))
    if (numero >0):
        sumaPositivos = sumaPositivos + numero
        cantidadPositivos += 1
    else:
        sumaNegativos += numero
print (f'Sumatoria de los negativos: {sumaNegativos}')
if (cantidadPositivos != 0):
    print (f'El promedio de los numeros positivos ingresados es {sumaPositivos/cantidadPositivos}')
else:
    print ('No se ingresaron numeros positivos')

#4. Cree una lista de sus canciones favoritas a saber sus mejores 5 y luego imprima en pantalla una a una. Al final a través de un numero aleatorio muestre alguna de las canciones
import random
canciones = ['Mi tesoro', 'Egoista', 'señal de vida', 'salgo pa la calle', 'camuflaje']
for cancion in canciones:
    print (cancion)
aleatorio = random.randint (0,4)
print (f'Se selecciono la siguiente cancion: {canciones[aleatorio]}')


