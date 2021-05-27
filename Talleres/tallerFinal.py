#Punto 1
mensaje_entrada = 'Hola, espero que te encuentres muy bien, calculare tu IMC'
pregunta_peso = 'Por favor ingresa tu peso en kg: '
pregunta_estatura = 'Excelente, ahora ingresa tu estatura en metros: '
pregunta_nombre = 'Cual es tu nombre?: '

print(mensaje_entrada)
isNombre = False
while (isNombre == False):
    try:
        ingresoNombre = input (pregunta_nombre)
        assert (ingresoNombre.isalpha())
        isNombre = True
    except:
        print ('Por favor ingresa un nombre valido, solo debe contener letras')

isDatoCorrect = False
while (isDatoCorrect == False):
    try:
        ingresoPeso = float (input(pregunta_peso))
        isDatoCorrect = True
    except ValueError:
        print ('El valor ingresado no es valido, debe contener unicamente numeros...')

isCorrect = False
while (isDatoCorrect == False):
    try:
        ingresoEstatura = float (input (pregunta_estatura))
        isDatoCorrect = True
    except AssertionError: 
        print ('El valor ingresado no es valido, debe contener unicamente numeros y punto (.) como indicador de decimales...')

IMC = ingresoPeso/(ingresoEstatura)**2
print (f'Tu IMC es de {IMC}')

#Punto 2
ingresoParrafo = input ('Ingresa un parrafo: ')
parrafo = ingresoParrafo.split (' ')
print (parrafo)
print (f'La palabra mas larga del texto ingresado es "{max(parrafo, key=len)}"')
print (f'La palabra mas corta del texto ingresado es "{min(parrafo, key=len)}"')

verificar = ingresoParrafo.endswith('.')
while (verificar == False):
    print('El parrafo que has ingresado no tiene punto (.) final, por favor ingresa el parrafo nuevamente...')
    ingresoParrafo = input ('Ingresa el parrafo: ')
    verificar = ingresoParrafo.endswith('.')

print ('Todo perfecto')

#Punto 3
import sys
nombreArchivo = 'mantenimientos.txt'

try:
    documento = open (nombreArchivo)

except FileNotFoundError:
    documento = open (nombreArchivo, 'w', encoding='UTF-8')
    descripcion = 'Se presenta informacion de nombre del equipo medico, una pequeña descripcion de este y su precio de mantenimiento'
    documento.writelines(descripcion)
    print ('El documento no existia, sin embargo ya ha sido creado...')
    sys.exit(1)

documento = open (nombreArchivo, 'a')

equipoBiomedico = input('Cual es el nombre del equipo biomedico?: ')
descripcionDeEquipo = input ('Ingrese una corta descripcion del equipo: ')
precioEquipo = float (input('Cual es el precio de mantenimiento: '))

documento.writelines('\n')
documento.writelines('\n' + equipoBiomedico)
documento.writelines('\n' + descripcionDeEquipo)
documento.writelines('\n' + str(precioEquipo))

documento.close()





