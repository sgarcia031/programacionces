def linedesign (cantidad = 50, patron = '-'):   
    print (patron * cantidad)

# 1. Crear una función que dado tres números muestre en pantalla la suma, la resta, la multiplicación, la división y la potencia entre ellos (ejem n1-n2-n3, n1/n2/n3, etc.)
def operaciones (valor1, valor2, valor3):
    suma = valor1 + valor2 + valor3
    resta = valor1 - valor2 - valor3
    division = valor1/valor2/valor3
    multiplicacion = valor1 * valor2 * valor3
    potenciacion = valor1 ** valor2 ** valor3
    print (f'La suma entre el primer valor dado con el segundo y tercero respectivamente tiene como resultado: {suma}')
    print (f'La resta el primer valor menos el segundo y su resultado menos el tercero  tiene como resultado: {resta}')
    print (f'La division el primer valor entre el segundo y su vez, este resultado dividido entre el tercero  tiene como resultado: {round (division,2)}')
    print (f'La multiplicacion del primer valor por el segundo y su vez, este resultado multiplicado por el tercero  tiene como resultado: {multiplicacion}')
    print (f'La potenciacion del primer valor elevando al segundo y su vez, este resultado elevado por el tercero  tiene como resultado: {potenciacion}')
#Ejemplos
operaciones (2,3,5)

preguntaValor1 =  int (input('Por favor ingrese un primer valor: '))
preguntaValor2 = int (input('Ahora ingrese un segundo valor: '))
preguntaValor3 = int (input('Por ultimo ingrese un tercer valor: '))
operaciones (preguntaValor1, preguntaValor2, preguntaValor3)
linedesign()

#2. Crear una función que dada tres listas del mismo tamaño las muestre en pantalla
def mostrar3Listas (lista1, lista2, lista3):
    for datos in range (len(lista1)):
        print (lista1 [datos], '\t', lista2 [datos], '\t', lista3 [datos])
#Ejemplo
listaNombres = ['Nombre', 'Juan', 'Pedro', 'Jacobo', 'Elisa', 'Sergio']
listaPesos = ['Peso', 67, 89, 77, 54, 69]
listaPorcentajeGrasa = ['% Grasa', 14, 18, 16, 15, 19]
mostrar3Listas (listaNombres, listaPesos, listaPorcentajeGrasa)
linedesign()

#3. Crear una función que calcule y devuelva el área de un triangulo, recuerde que la formula del mismo es (base*altura) /2. Pida las entradas que considere necesarias
def areaTriangulo (base, altura):
    area = (base * altura)/2
    print (f'El area del triangulo es {round (area,2)} cm^2')
#Ejemplo
preguntaBase = float (input('Ingrese la longitud de la base del triangulo en cm: '))
preguntaAltura = float (input('Cual es la altura del triangulo?: '))
areaTriangulo(preguntaBase, preguntaAltura)
linedesign()

#4. Crear una función que dada una lista de números enteros muestre el promedio, el máximo, el mínimo.
def maxMinPro (lista):
    mayor = max(lista)
    menor = min(lista)
    sumaDatos = 0
    for datos in lista:
        sumaDatos += datos
    promedio = sumaDatos/len(lista)
    print(f'El mayor dato registrado de la lista es {mayor}, el menor dato es {menor} y el promedio de todos los datos es {round(promedio,2)}')
#Ejemplo
listaTemperaturas = [37,36.5,33,36,39]
maxMinPro(listaTemperaturas)
linedesign()

#5. 
def suceFibo (valorPedido):
    valorX = 0
    valorY = 1
    for sucesion in range (valorPedido-1):
        sumaXY = valorX + valorY
        valorX, valorY = valorY, sumaXY
    return (sumaXY)

preguntaNumeroSucesion = int (input('Por favor ingrese el numero de la posicion en la sucesion que desea ver:'))
posicion = suceFibo(preguntaNumeroSucesion)
print (posicion)


