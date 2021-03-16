
mensaje_menu = '''
    Buen dia, ingrese el numero correspondiente para ejercer la accion propuesta: 
    1. Convertir las temperaturas de grados centigrados a otra unidad de temperatura
    2. Mostrar lista del estado de los pacientes
    3. Mostrar temperatura maxima y minima
    4. Salir del programa
'''
opcion_Temperatura = '''
    C. Celsius
    K. Kelvin
    F. Fahrenheit
A que unidad de temperatura desea convertir los datos: '''

mensaje_Error = 'Por favor ingrese una entrada valida...'
mensaje_Despedida = 'Muchas gracias, ten un feliz dia!'
#---Calculos Preliminares---#
Temperatura_Corporal = [36, 37 ,38 ,35 ,36 ,38 ,37.5 ,38.2 ,41 ,37.4, 38.6, 39.1, 40.3, 33]
listaFahrenheit = []
listaKelvin = []
listaClasificacion = []

#Paso de datos a Kelivin
for datos in Temperatura_Corporal:
    kelvin = round (datos + 273.15,2)
    listaKelvin.append (kelvin)

#Paso de datos a Fahrenheit
for datos in Temperatura_Corporal:
    Fahrenheit = round ((datos * 1.8) + 32,2)
    listaFahrenheit.append (Fahrenheit)

#Clasificar estado de salud
for datos in Temperatura_Corporal:
    estado = ''
    if (datos < 36):
        estado = 'Hipotermia'
    elif (datos >= 36 and datos <= 37.5):
        estado = 'Normal'
    else:
        estado = 'Fiebre'
    listaClasificacion.append (estado)
#Temperatura Max y min
mayor = max(Temperatura_Corporal)
menor = min(Temperatura_Corporal)
#---Bonus---#
PromedioDeTiempo = round (24/len(Temperatura_Corporal),2)

#---Entrada codigo---#
ingreso_Menu = int (input(mensaje_menu))

while (ingreso_Menu != 4):
    if (ingreso_Menu == 1):
        print (f'Usted ha ingresado la opcion {ingreso_Menu}')
        ingreso_unidad = input (opcion_Temperatura)
        if (ingreso_unidad == 'C' or ingreso_unidad == 'c'):
            print ('No es necesaria la conversion de datos, pues ya se encuentran en Celsius; de igual forma aqui se encuentra la lista:')
            print (Temperatura_Corporal)
            ingreso_Menu = int (input(mensaje_menu))
        elif (ingreso_unidad == 'K' or ingreso_unidad == 'k'):
            print ('Aqui tiene la lista de los datos en kelvin en su posicion respectiva: ')
            print (listaKelvin)
            ingreso_Menu = int (input(mensaje_menu))
        elif (ingreso_unidad == 'F' or ingreso_unidad == 'f'):
            print ('Aqui tiene la lista de los datos en Fahrenheit en su posicion respectiva: ')
            print (listaFahrenheit)
            ingreso_Menu = int (input(mensaje_menu))
        else:
            print ('Entrada no valida, por favor ingrese una opcion valida')
    elif (ingreso_Menu == 2):
        print (f'Usted ha ingresado la opcion {ingreso_Menu}, aqui encontrara una lista del estado de salud en la misma posicion del ingreso de los datos:')
        print (listaClasificacion)
        ingreso_Menu = int (input(mensaje_menu))
    elif (ingreso_Menu == 3):
        print (f'Usted ha ingresado la opcion {ingreso_Menu}')
        print (f'La mayor temperatura registrada en celsius es: {mayor}')
        print (f'La menor temperatura registrada en celsius es: {menor}')
        print (f'En promedio se tomo un dato cada {PromedioDeTiempo} horas en todo el dia')
        ingreso_Menu = int (input(mensaje_menu))
    else:
        print (mensaje_Error)
        ingreso_Menu = int (input(mensaje_menu))

print (mensaje_Despedida)







