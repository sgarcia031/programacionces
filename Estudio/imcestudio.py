#---MENSAJES---#
MENSAJE_BIENVENIDA = "Hola! calculare tu Indice de masa corporal"
MENSAJE_RESPUESTA = "Tu IMC es: "
MENSAJE_FLACO = "Necesitas comer mas"
MENSAJE_NORMAL= "Estas en forma, sigue asi"
MENSAJE_SOBREPESO= "Te sobran algunos kilos, deja de comer tanto y ponte a hacer ejercicio"
MENSAJE_OBESO = "Estas obeso, parate ya de la cama y cuida tu salud"
#---preguntas---#
PREGUNTA_PESO = "Cuanto pesas en kilogramos?: " 
PREGUNTA_ESTATURA = "Cuanto mides en metros?: "
#---Entrada codigo---#
print (MENSAJE_BIENVENIDA)
peso = float (input (PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso/ (estatura)**2
print (MENSAJE_RESPUESTA, imc)
#---Condicionales---#
if (imc < 18.5):
    print(MENSAJE_FLACO)
elif (imc >= 18.5 and imc <25):
    print (MENSAJE_NORMAL)
elif (imc >= 25 and imc < 30):
    print (MENSAJE_SOBREPESO)
else:
    print (MENSAJE_OBESO)



