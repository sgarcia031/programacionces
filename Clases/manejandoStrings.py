#Repaso listas
texto = 'Hola, espero que todo ande bien'
lista = [1,43,554,23,2,2]
lista.sort()  #organizar en orden
print(lista)

lista.pop(2) #Eliminar 

for elemento in lista:
    print (elemento)
for i in range (len(lista)):
    print(lista[i])

for letra in texto:
    print (letra)

print (texto [1]) #Toma el segundo elemento de la lista del texto (en este caso seria la o)
palabras = texto.split ('') # Separa los elementos en los espacios
print (palabras)

eliminarE = texto.split ('e')
texto.split()
print (eliminarE)

#Ejemplo
datos = 'nombre;apellido;edad'
print(datos.split(';'))

#Como podemos hacer para unir algo que ya se separo
uniendo = ''.join(eliminarE)
print (uniendo)
info = ' '.join(datos.split(';')) #Lo hace todo a la vez
print(info)

listaNombre = ['Laura','Juan','Mario', 'Elsa', 'Katherine', 'daniel']  #OJO: Las letras minusculas tienen mas valor, por ello si coloco daniel --> aparecera como si fuese el mayor. Cada letra tiene un valor
print (max(listaNombre))
print(max(listaNombre, key=leg)) #Lo va a calcular pero con el tamaño de la palabra (numero de letras)

respuesta = input('Ingrese Si o No: ')
if respuesta.upper() == 'SI':
    print ('Hola, bienvenido al programa')
else:
    print ('Chao!')
######

nombre = input('Ingrese su nombre: ')
print (nombre.capitalize()) #Lo pone con mayuscula (la priemer palabra)

correo = 'ESPERO QUE ESTES BIEN'
print (correo.casefold().capitalize()) #Lo vuelve todo en mayuscula y despues pone en mayuscula la primera

saludo = 'Hola, como estas?'
nombre = 'Maria Alejandra'
#Como ponemos mayuscula a dos palabras en una misma frase?
nombre1 = 'maria alejandra'
nombres = nombre1.split(' ')
nombre = ''
for elemento in nombres: 
    nombre += elemento.capitalize() + ' '
print (nombre)


print(saludo.center(50)) #Contando el numero de caracteres que tiene la palabra 

enunciado = 'Hola, hola, ya me canse de decir tantos hola'
print (enunciado.count ('hola')) #Me dice cuantos hola hay en el texto

print (enunciado.upper().count('HOLA')) #La convierte en mayuscula para evitar que no se cuente en caso de que se presente una mayuscula

print (enunciado.find('decir')) #Da la poscion en la que se encuentra

print(enunciado[25:30]) #Hasta el 29 en realidad ya que no incluye el ultimo

txt = 'Me gusta programar en Java'
print(txt.replace('Java', 'Python')) #Reemplaza la primer parabra ingresada por la segunda

numeroID = '1234342'
print(numeroID.isnumeric()) #Devuelve verdadero o falso si es completamente numerico

parrafo = 'sdhas saifhas spdhapd wqhjda'
print (parrafo.endswith('.')) #Devuelve verdadero o falso