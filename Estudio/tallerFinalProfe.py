###PUNTO 1###
def validateFloat (pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = float (input(pregunta))
            isCorrectData = True
        except ValueError:
            print('Los datos ingresados son incorrectos, ingreselos nuevamente...')
    return valor

#Uso

def validateString (pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = (input(pregunta))
            assert (valor.isalpha())
            isCorrectData = True
        except AssertionError:
            print('Los datos ingresados son incorrectos, ingreselos nuevamente...')
    return valor

def pedirDatosEPN ():
    '''
        Se le pide al usuario el peso, la estatura
        y el nombre, validando que los datos esten 
        correctos
    '''
    preguntaPeso = 'Ingrese su peso en kg: '
    preguntaEstatura = 'Ingrese su estatura en metros: '
    preguntaNombre = 'Ingrese su nombre: '
    peso = validateFloat(preguntaPeso)
    estatura = validateFloat(preguntaEstatura)
    nombre = validateString(preguntaNombre)
    return peso, estatura, nombre


def calcularIMC ():
    pesoIn, estaturaIn, nombreIn = pedirDatosEPN()
    imc = pesoIn/ (estaturaIn**2)
    return imc, nombreIn

imc, nombre = calcularIMC()
print (imc, nombreIn)
print (f'El imc de {nombre} es de {imc} %')

###PUNTO 2###

def validateEndwith (strValidate, pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert (valor.endwiths(strValidate))
            isCorrectData = True
        except AssertionError:
            print(f'Los datos ingresados son incorrectos, ingreselos nuevamente y recuerde que debe terminar con "{strValidate}"...')
    return valor

parrafo = validateEndwith('.', 'Ingrese un parrafo: ')
parrafo = parrafo [:-1] #Todo menos la ultima posicion 
palabras = parrafo.split(' ')
print (palabras[-1], palabras [-1][:-1])
print (palabras)

print(f'La palabra mas grande es "{max(palabras,key=len)}" y el menor es "{min(palabras, key=len)}"')

#Quitar comas
parrafo = 'Hola, como estas, bien y tu'
parrafo = parrafo.replace (',', ' ')
print (parrafo)
palabrasParrafo = parrafo.split(' ')

###PUNTO 3###
import sys
def validarArchivo (nombreArchivo, descripcion):
    try:
        archivo = open (nombreArchivo)
        print ('1')
        return True
    except FileNotFoundError:
        archivo = open(nombreArchivo,'w', encoding = 'UTF-8')
        descripcion = 'Archivo de datos de estudiantes'
        print ('2')
        archivo.writelines(descripcion)
        sys.exit(1)
        return False

def guardarLinea (nombreArchivo, lineaIn):
    archivo = open (nombreArchivo, 'a')
    archivo.writelines ('\n'+lineaIn)

nameFile = 'mantenimientos.txt'
isValidate = validarArchivo(nameFile, 'Seguimiento de mantenimiento de equipos medicos')
if(isValidate == True):
    descEquipo = input ('Ingrese la descripcion del equipo: ')
    nombre = validateString('Ingrese el nombre del equipo: ')
    precio = validateFloat ('Ingrese el precio: ')
    linea = descEquipo + ' Nombre Tecnico: ' + nombre + ' Precio acordado: ' + str(precio)
    guardarLinea (nameFile, linea)
else:
    print ('Se creo el archivo')