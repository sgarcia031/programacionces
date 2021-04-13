import conversorTemperaturas  as ct
import clasefunciones as cf
preguntaOpcion = '''Ingrese alguna de estas opciones...
    1.Convertir Temperaturas
    2.Mostrar clasificacion
    3.Mostrar topes
    4.Salir
''' 

preguntaTemperatura = '''
    K- Mostrar en Kelvin
    F- Mostrar en Fahrenheit
    C- Mostrar en Celcius
'''

mensajeCelcius = 'Mostrando lista original'
mensajeFahrenheit = 'Mostrando lista en F'
mensajeKelvin = 'Mostrando lista en K'
mensajeDespedida = 'Que tengas un buen dia'

mensajeErrorEntrada = 'Valor ingresado no valido'
temperaturaCorporal = [36, 37 ,38 ,35 ,36 ,38 ,37.5 ,38.2 ,41 ,37.4, 38.6, 39.1, 40.3, 33]
#Punto 1
temperaturaCorporalFahrenheit = ct.conversionTemperatura(temperaturaCorporal, 'F')
print(temperaturaCorporalFahrenheit) 

cf.linedesign(15, '#')
temperaturaCorporalKelvin = ct.conversionTemperatura(temperaturaCorporal, 'K')
print(temperaturaCorporalKelvin) 

cf.linedesign(15, '#')
#Punto 2
clasificacionTemperaturas = ct.clasificarTemperaturas(temperaturaCorporal)
print(clasificacionTemperaturas)

#Punto 3
opcionEscogida = int(input(preguntaOpcion))
while (opcionEscogida != 4):
    #------Opcion 1------#
    if (opcionEscogida == 1):
        OpcionMoneda = input (preguntaTemperatura) 
        if (OpcionMoneda == 'C'): 
            print ('la conversion no era necesaria')
            print (mensajeCelcius)
            cf.mostrarLista (temperaturaCorporal)
        elif (OpcionMoneda == 'F'):
            print (mensajeFahrenheit)
            cf.mostrarLista(temperaturaCorporalFahrenheit)
        elif (OpcionMoneda == 'K'):
            print (mensajeKelvin)
            cf.mostrarLista(temperaturaCorporalKelvin)
        else: 
            print ('Por favor ingrese una opcion valida')
    #------Opcion 2-----#
    elif (opcionEscogida == 2):
        print('Mostrando conversion')
        print('Grados C', '\t', 'Clasificacion' )
        cf.mostrar2Listas(temperaturaCorporal, clasificacionTemperaturas)
    #------Opcion 3-----#
    elif (opcionEscogida == 3):
        ct.mostrarTopes(temperaturaCorporal)
    #------Opcion 4-----#
    elif (opcionEscogida == 4):
        print(mensajeDespedida)
    #------Opcion No valida-----#
    else:
        print ('Respuesta no valida')