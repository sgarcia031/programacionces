import sys 

nombre = input ('Ingrese su nombre: ')
edad = int (input('Ingrese su edad: '))
estatura = float (input('Ingrese su estatura: '))

#Guardarlo en .txt

nombreArchivo = 'estudiantes.txt'

try:
    archivo = open(nombreArchivo) # Por defecto se va con 'r' crea el archivo solo abierto a lectura
    print ('1')
except FileNotFoundError: #Como no existia, lo creamos
    archivo = open (nombreArchivo, 'w', encoding= 'UTF-8') #w --> FORMA DE SOBREESCRIBIR LO QUE YA ESTA ESCRITO (Se usa mas el x, w, y)
    print ('2')
    descripcion = 'Archibo de datos de estudiantes'
    archivo.writelines(descripcion)
    sys.exit(1) #Para cerrar ejecucion, despues ya entraria por el try

archivo = open(nombreArchivo, 'a') #Es necesario ponerse para que el archivo este abierto para dicionar informacion
#Escribir linea sobre ese archivo
linea = '\nNombre: ' + nombre +' Edad '+ str (edad) + ' Estatura ' + str (estatura)
        #\n --> enter

archivo.writelines(linea) #Linea debe ser un str
archivo.close()

#leer, mostrar archivos 
with open (nombreArchivo) as reader:
    for line in reader:
        print(line)

import pandas as pd
diccionario = {}
diccionario ['Nombre'] = 'Daniel'
diccionario['Edad'] = 27
diccionario['Estatura'] = 1.67
serie = pd.Series (diccionario)
print(serie)
serie.to_csv()