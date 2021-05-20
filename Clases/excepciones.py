isCorrectInfo = False #Para ahorrarse una pregunta)
while (isCorrectInfo == False): 
    try:
        edad = int (input('Ingrese su edad: '))
        isCorrectInfo = True  #Para que se salga del while
    except ValueError: 
        print ('Ingresaste un dato no valido')


#Leer un archivo
nombreArchivo = input ('Ingrese el nombre del archivo que desea encontrar: ')
try:
    archivo = open('hola.txt')
except FileNotFoundError: #Tipo de error Lo que sale cuando no se reconoce el archivo --> cuando el programa marca error
    print(f'El archivo {nombreArchivo} no se ha encontrado')

base = 4
divisor = 0
try:
    dividir = base/divisor
except ZeroDivisionError: 
    print ('El divisor ingresado es igual a cero, por lo tanto es imposible dividir')

nombre = 'Samuel'
print (nombre.isalpha())  #Si se le ingresa un numero aparece como falso (si es letras o no)

assert (nombre.isalpha())  #Cuando necesito en el codigo que 2 cosas sean iguales, que tengan que ser asi

isCorrectIn = False
while (isCorrectIn == False):
    try:
        nombre = input ('Ingrese su Nombre: ')
        assert (nombre.isalpha())
        isCorrectIn = True
    except AssertionError:
        print ('Ingrasaste un dato no valido')

while (isCorrectInfo == False): 
    try:
        edad = int (input('Ingrese su edad: '))
        assert (edad >= 18)
        isCorrectInfo = True
    except AssertionError: 
        print ('Los menores de edad no pueden acceder')
    except ValueError:
        print ('Las edades son numeros enteros')

###Listas

listas = [2, 43, 45, 21]
try:
    listas [5] #Splp llega a posicion 3
except IndexError: 
    print ('El indice es mayor al tamaño de la lista')
