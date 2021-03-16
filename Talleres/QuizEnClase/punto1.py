listaPesos = [20000, 30000, 4000, 2500, 1000, 7600]
preguntaMoneda = '''
    C- Mostrar original en pesos colombiano
    D- Mostrar en Dolares
    E- Mostrar el Euros
'''
listaEuros = []
for elemento in listaPesos:
    conversor = round (elemento *0.00023,2) #Redondear un numero a la cantidad de digitos que estan despues de la ,
    listaEuros.append (conversor)
listaDolares  = []
for elemento in listaPesos:
    conversor = round (elemento *0.00028,2)
    listaEuros.append (conversor)

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