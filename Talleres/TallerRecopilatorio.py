listaDolares = [20000, 30000, 4000, 2500, 1000, 7600]
Mensaje_Bienvenida = '''
    1. Convertir lista de dolares a otra moneda
    2. Clasificar la categoria dependiendo de los ingresos
    3. Mostrar ingreso mas alto, mas bajo y el promedio de los ingresos
    4. Salir del programa

Buen dia, ingrese la opcion que desee realizar:'''

Mensaje_convertir_D = '''A cual moneda desea cambiar los valores:
    C. Pesos colombianos (COP)
    E. Convertir en Euros (EUR)
'''
#---Codigo---#
menu = int (input(Mensaje_Bienvenida))

listaPesos = []
listaEuros = []
listaClasificacion = []
#---Opcion 1/Pesos---#
for valor in listaDolares:
    pesos = valor * 3700
    listaPesos.append (pesos)
#---Opcion 1/Euros---#
for valor in listaDolares:
    euros = valor * 0.84
    listaEuros.append (euros)

#---Opcion 2---#
for ingresos in listaDolares:
    clasificacion = ''
    if (ingresos < 1000):
        clasificacion = 'Ingresos Bajos'
    elif (ingresos >= 1000 and ingresos < 7000):
        clasificacion = 'Ingresos medios'
    elif (ingresos >= 7000 and ingresos < 20000):
        clasificacion = 'Ingreos altos'
    else:
        clasificacion = 'Ingresos elevados'
    listaClasificacion.append (clasificacion)

#---Opcion 3---#
mayor = max (listaDolares)
menor = min (listaDolares)
acumulado = 0 
for ingreso in listaDolares:
    acumulado += ingreso
promedio = acumulado/len(listaDolares)
#---Si se quiere redondear el resultado---#
promedioDolares = round (promedio,2)

#Menu
while (menu != 4):
    if (menu ==1):
        print (f'Usted eligio la opcion {menu}')
        conversion = input (Mensaje_convertir_D)
        if (conversion == 'C'):
            print (listaPesos)
        elif (conversion == 'E'):
            print (listaEuros)
        else:
            print ('Por favor ingrese una entrada valida')

    elif (menu ==2):
        print (f'Usted escogio la opcion {menu}')
        print (listaClasificacion)
    
    elif (menu == 3):
        print (f'Usted escogio la opcion {menu}')
        print (f'El ingreso maximo fue {mayor}')
        print (f'El ingreso minimo fue {menor}')
        print (f'El promedio de los ingresos es {promedioDolares}')
    else:
        print ('Por favor ingrese una opcion valida')
        menu = int (input(Mensaje_Bienvenida))
    
print ('Gracias por participar')



