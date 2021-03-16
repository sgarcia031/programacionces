listaPesos = [20000, 30000, 4000, 2500, 1000, 7600]
PreguntaBorrarCoordenada = 'Ingrese la posicion que desea borrar'
print (listaPesos)
posicion = int (input(PreguntaBorrarCoordenada)) - 1
listaPesos.pop (posicion) #borra valor en la posicon que se escogio
print (listaPesos)