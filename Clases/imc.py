#---Constantes---#
PREGUNTA_PESO = "Cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "Cuanto mides en m? : "
MENSAJE_BIENVENIDA = "Hola! como estas? Voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es: "

#---Entrada codigo---#
print (MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso/(estatura)**2
print(MENSAJE_DESPEDIDA, imc)

isObeso = imc >= 30
print ("El resultado de la purueba de obesidad es ...", isObeso)

