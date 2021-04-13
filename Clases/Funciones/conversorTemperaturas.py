def conversionTemperatura (temperaturas,unidad):
    '''
Convierte una lista de temperaturas segun la unidad ingresada, puede ser:
    Entradas:
        K--> Kelvin
        F--> Fahrenheint
    Temperaturas: lista temperaturas en grados centigrados
    Retorna:
    Si se ingresa un valor invalido, devolvemos None...
    Devuelve la lista convertida en las unidades deseadas
    '''
    listaConvertida = []
    
    for temperatura in temperaturas:
        conversion = None
        if unidad == "F":
            conversion = temperatura *1.8 + 32
        elif unidad == 'K':
            conversion = temperatura + 273.15
        else:
            listaConvertida = None
    listaConvertida.append(round(conversion, 2))
    return listaConvertida 

def clasificarTemperaturas (temperaturas):
    '''Retorna la clasificacion de las temperaturas ingresadas,
    deben estar en grados centigrados
    '''

    listaClasificacion = []
    estado = None
    for temperatura in temperaturas:
        if temperatura < 36:
            estado = 'Hipotermia'
        elif temperatura >= 36 and temperatura < 37.6:
            estado = 'Normal'
        else:
            estado = 'Fiebre'
        listaClasificacion.append (estado)
    return listaClasificacion

def mostrarTopes(lista):
    '''Muestra los datos registrados'''
    mayor = max(lista)
    menor = min (lista)
    periodoHoras = len(lista)
    print ('La mayor temperatura registrada es', mayor)
    print ('La menor temperatura registrada es', menor)
    print ('El promedio de las temperaturas registrada es', periodoHoras)
