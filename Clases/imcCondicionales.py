#---Constantes---#
PREGUNTA_PESO = "Cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "Cuanto mides en m? : "
MENSAJE_BIENVENIDA = "Hola! como estas? Voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es: "
MENSAJE_BAJO_PESO = "Estas pero delgado! "
MENSAJE_PESO_NORMAL = "Estas en forma"
MENSAJE_SOBREPESO = "Estas en sobrepeso, deja de comer tanto"
MENSAJE_OBESO = "Cuidate, parate de la cama y a correr, eres obeso"

#---Entrada codigo---#
print (MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso/(estatura)**2
isBajopeso = imc < 18.5
isNormal = imc >= 18.5 and imc < 25
isSobrepeso = imc >= 25 and imc < 30
resultado = ""
if (isBajopeso):
    resultado = MENSAJE_BAJO_PESO
elif (isNormal):
    resultado = MENSAJE_PESO_NORMAL
elif (isSobrepeso):
    resultado = MENSAJE_SOBREPESO
else:
    resultado = MENSAJE_OBESO
print (MENSAJE_DESPEDIDA, imc)
print (resultado)