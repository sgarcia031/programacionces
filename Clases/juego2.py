import random
#---Entrada---#
MENSAJE_SEGUNDO_NIVEL = 'Felicidades, pasaste el primer nivel, ahora pasaras al segundo, buena suerte...'
MENSAJE_BIENVENIDA = '''
            Bienvenido a este programa
                    ¡Juguemos!'''
MENSAJE_FRIO = 'Estas frio'
MENSAJE_CALIENTE = 'Estas Caliente'
PREGUNTAR_NUMERO = '''
        En este juego debes asertar un numero 
        que va del 1 al 10, lo puedes intentar
        las veces que decidas mediante la dificultad...
        Muchos exitos, ingresa tu numero:
'''
PREGUNTAR_NUMERO_2 = '''Ahora ingresa otro numero para pasar el ultimo nivel: '''
PREGUNTA_DIFICULTAD = '''
    1. Facil: Tendras 10 vidas
    2. Moderado: Tendras 5 vidas
    3. Dificil: Tendras 2 vida
'''
PREGUNTA_FALLIDA = 'Ohhh, fallaste, sigue intentando, ingresa otro numero: '
MENSAJE_GANASTE = 'Felicidades! Acertaste...'
MENSAJE_PERDISTE = 'Perdiste, lo lamento...'
#---Entrada codigo---#
numeroOculto = random.randint (1,10)
numeroOcultoDos = random.randint (1,10)
vidas = None


dificultad = int (input (PREGUNTA_DIFICULTAD))
while (dificultad != 1 and dificultad != 2 and dificultad !=3):
    print ('ingrese una opcion valida')
    dificultad = int (input(PREGUNTA_DIFICULTAD))


if ( dificultad == 1):
    vidas = 10
    print('Modo facil activado')

elif (dificultad == 2):
    vidas = 5
    print('Modo moderado activado')
else:
    vidas = 2
    print('Modo Dificil activado')

numeroIngresado = int (input(PREGUNTAR_NUMERO))
while (numeroIngresado != numeroOculto and vidas > 1):
    if (numeroIngresado > numeroOculto-3 and numeroIngresado < numeroOculto+3):
        print (MENSAJE_CALIENTE)
    else:
        print(MENSAJE_FRIO)
    vidas -= 1
    print (f'Te quedan {vidas} vidas')
    numeroIngresado = int (input(PREGUNTA_FALLIDA))

if (vidas > 0 and numeroIngresado == numeroOculto):
    print (MENSAJE_SEGUNDO_NIVEL) 
    numeroIngresado = int (input(PREGUNTAR_NUMERO_2))
    while (numeroIngresado != numeroOcultoDos and vidas > 0):
        if (numeroIngresado > numeroOcultoDos - 3 and numeroIngresado < numeroOcultoDos + 3):
            print(MENSAJE_CALIENTE)
        else:
            print (MENSAJE_FRIO)
        vidas -=1
        print (f'Te quedan {vidas} vidas')
        numeroIngresado = int(input(PREGUNTA_FALLIDA))
else:
    print (MENSAJE_PERDISTE, 'El numero era el', numeroOculto)

if (vidas > 0 and numeroIngresado == numeroOcultoDos):
    print (MENSAJE_GANASTE)
else:
    print (MENSAJE_PERDISTE, 'El numero era el', numeroOcultoDos)


