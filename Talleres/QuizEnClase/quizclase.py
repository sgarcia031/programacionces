preguntaOpcion = '''Ingrese alguna de estas opciones...
    1.Hacer conversion de pesos a dolares o Euros
    2.Agrege un valor a la lista de pesos
    3.Mostrar valor mas alto, mas bajo y promedio.
    4.Eliminar un elemento de la lista
    5.Salir
'''
preguntaMoneda = '''
    C- Mostrar original en pesos colombiano
    D- Mostrar en Dolares
    E- Mostrar el Euros
'''
preguntarNumero = 'Ingrese un valor en COP: '
PreguntaBorrarCoordenada = 'Ingrese la posicion que desea borrar'
mensajeMayor = 'El mayor numero ingresado es: '
mensajeMenor = 'El menor numero ingresado es: '
mensajePromedio = 'El promedio de los numeros es: '
#---Conversion punto 1---#
listaPesos = [20000, 30000, 4000, 2500, 1000, 7600]
listaEuros = []
for elemento in listaPesos:
    conversor = round (elemento *0.00023,2) #Redondear un numero a la cantidad de digitos que estan despues de la ,
    listaEuros.append (conversor) #append --> coge uno por uno
listaDolares  = []
for elemento in listaPesos:
    conversor = round (elemento *0.00028,2)
    listaEuros.append (conversor)

opcionEscogida = int (input (preguntaOpcion))
while (opcionEscogida != 5):
    #------Opcion 1------#
    if (opcionEscogida == 1):
        OpcionMoneda = input (preguntaMoneda)
        if (OpcionMoneda == 'C'): 
            print ('Mostrando lista original')
            print (listaPesos)
        elif (OpcionMoneda == 'D'):
            print ('Mostrando lista en Dolares')
            print (listaDolares)
        elif (OpcionMoneda == 'E'):
            print ('Mostrando lista en Euros')
            print (listaEuros)
        else: 
            print ('Por favor ingrese una opcion valida')
    #------Opcion 2-----#
    elif (opcionEscogida == 2):
        valorIngresado = float (input(preguntarNumero))
        listaPesos.append (valorIngresado)
        print (listaPesos)
    #------Opcion 3-----#
    elif (opcionEscogida == 3):
        print (mensajeMayor, max(listaPesos))
        print (mensajeMenor, min (listaPesos))
        print (mensajePromedio, sum(listaPesos)/len (listaPesos))
    #------Opcion 4-----#
    elif (opcionEscogida == 4):
        print (listaPesos)
        posicion = int (input(PreguntaBorrarCoordenada)) - 1
        listaPesos.pop (posicion) 
        print (listaPesos)
    #------Opcion No valida-----#
    else:
        print ('Respuesta no valida')
    opcionEscogida = int (input (preguntaOpcion))
print ('Feliz dia')


