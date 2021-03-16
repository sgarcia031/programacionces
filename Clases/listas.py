nombres =['Santi', 'Samuel', 'Aleja', 'Elsa']
print (type(nombres)) 
print (nombres[2])
nombres.append ('Mauricio')
print (nombres)
print (nombres[2])
edades= [18,19,20,21,22,15,13,16]
estaturasn= [1.62,1.70, 1.80, 1.98]
#al ultimo
print(edades[-2])
print(edades[0:2]) #incluye el cero pero no el 2
print(edades [:3])
print(edades [2:])
print(edades [:])
edades.sort () #ordenar la lista de edades
print(edades)
edades.sort(reverse=True) #Forma descendente
print(edades)
mayor = max (edades) #numero max
print(mayor)
menor = min (edades)  #numero min
print(menor)
#Como contamos cuantos elementos hay
largoListaEdades = len(edades)
print (largoListaEdades)
#Como sumamos elementos
sumaEdades = sum(edades)
print (sumaEdades)
#Calcular promedio
promedioEdades = sumaEdades/largoListaEdades
print (promedioEdades)
#Eliminar elemento de lista --> lista.pop
edades.pop(2)
print (edades)

## Ciclo FOR y LISTAS
largoListaEdades = len(edades)
for indice in range (largoListaEdades):
    print (edades[indice])  #empieza en poscision cero --> edades[cero], edades[uno] ...
    print ('estoy en la posicion', indice, 'valgo', edades[indice])
largoListaNombres = len (nombres)
for indice in range (largoListaNombres):
    print (nombres[indice])

posicionesConValoresPares = []
largoListaEdades= len(edades)
for posicion in range (largoListaEdades):
    if (edades[posicion]%2 == 0):
        posicionesConValoresPares.append(posicion)
print (edades)
print (posicionesConValoresPares)

#Solo cuando interese mostrar la lista
posicion = 0
for edad in edades:
    print (edad)

for nombre in nombres:
    print (nombre)
    print (posicion)
    posicion +=1

posicion = 0
posicionesPares = []
for edad in edades:
    if (edad%2 == 0):
        posicionesPares.append(posicion)
    posicion +=1
    print
