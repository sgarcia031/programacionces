import parcial1 as p1

#Ejemplo
p1.operaciones(2,3,4)

def suceFibo (valorPedido):
    valorX = 0
    valorY = 1
    for sucesion in range (valorPedido-2):
        sumaXY = valorX + valorY
        valorX, valorY = valorY, sumaXY
    return (sumaXY)

preguntaNumeroSucesion = int (input('Por favor ingrese el numero de la posicion en la sucesion que desea ver:'))
posicion = suceFibo(preguntaNumeroSucesion)
print (posicion)
