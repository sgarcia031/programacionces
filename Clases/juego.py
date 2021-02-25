#---Entrada---#
MENSAJE_BIENVENIDA = '''
            Bienvenido a este programa
                    Juguemos!'''
PREGUNTAR_NUMERO = '''
        En este juego debes asertar un numero 
        que va del 1 al 10, lo puedes intentar
        solo 3 veces...
        Muchos exitos, ingresa tu numero: '''

PREGUNTAR_FALLIDA = 'Ohhh, fallaste, sigue intentando, ingresa otro numero: '
MENSAJE_GANASTE = 'Felicidades! Acertaste...'
MENSAJE_PERDISTE = 'Perdiste, lo lamento...'
#---Entrada codigo---#
numeroOculto = 7
vidas = 3
numeroIngresado = int (input (PREGUNTAR_NUMERO))
if (numeroIngresado != numeroOculto):
    vidas-=1
while (numeroOculto != numeroIngresado and vidas > 0):
    numeroIngresado = int (input(PREGUNTAR_FALLIDA))
    vidas -=1
if (vidas >= 0 and numeroIngresado == numeroOculto):
    print (MENSAJE_GANASTE)
    print (vidas)
else: 
    print (MENSAJE_PERDISTE, 'El numero era', numeroOculto)

