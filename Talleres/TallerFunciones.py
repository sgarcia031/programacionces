def linedesign (cantidad = 30, patron = '-'):   
    print (patron * cantidad)

#Punto 1
def mostrarListaPorLinea (lista):
    for elementos in lista:
        print (elementos)

listaPesos = [67,56,98,78,65,76]
mostrarListaPorLinea(listaPesos)

linedesign()
#Punto 2
def mayorMenorPromedio (lista):
    mayor = max (lista)
    menor = min (lista)
    sumalista = 0
    for datos in lista:
        sumalista += datos
    promedio = sumalista/len(lista)

    print (f'El promedio de la lista es {round(promedio,2)}, teniendo como dato mayor {mayor} y dato menor {menor}...')

mayorMenorPromedio(listaPesos)

linedesign()
#Punto 3
def numeroSaludos (cantidad):
    print ('Muy buenas ' * cantidad)

numeroSaludos (10)

linedesign()
#Punto 4
def numerosPares (lista):
    listaPares = []
    for pares in lista:
        if (pares % 2 == 0):
            listaPares.append(pares)
    print (f'Los numeros pares de la lista son: {listaPares}')

numerosPares(listaPesos)

linedesign()
#Punto 5
def mayoresQue24 (lista):
    mayoreslista = []
    for datos in lista:
        if (datos > 24):
            mayoreslista.append (datos)
    print (f'Los datos con valores superiores a 24 son: {mayoreslista}')

mayoresQue24(listaPesos)

linedesign()
#Punto 6
def calcularimc (peso, altura):
    imc = peso/(altura**2)
    print (f'El IMC de la persona es: {imc}')

preguntaAltura = float (input('Por favor ingrese su estatura en metros: '))
preguntaPeso = float (input('Ahora ingrese su peso en Kilogramos: '))

calcularimc (preguntaPeso, preguntaAltura)

linedesign()
#Punto 7
def despedida (nombre):
    print (F'Hasta luego {nombre}, que tengas un buen dia!')

despedida('Samuel')
