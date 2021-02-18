#---Constantes---#
MENSAJE_BIENVENIDA = "Binevenido, averiguaremos que seas menor de edad"
MENSAJE_EDAD_MAYOR = "Eres mayor de edad, puedes seguir correctamente"
MENSAJE_EDAD_MENOR = "Eres menor de edad, no puedes seguir"
PREGUNTA_EDAD = "Cuantos años tienes?"

#---Entradas al codigo---#
print (MENSAJE_BIENVENIDA)
edad = int (input(PREGUNTA_EDAD))
isMayor = edad >= 18
resultado = ""
if (isMayor):
    resultado = MENSAJE_EDAD_MAYOR
else:
    resultado = MENSAJE_EDAD_MENOR

print (resultado)