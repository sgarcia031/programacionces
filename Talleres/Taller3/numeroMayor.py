# Determinar cual numero es mayor
#---Preguntas---#
P_numeroA = "Ingrese un numero entero: "
P_numeroB = "Excelente! Ahora ingrese otro numero: "
#---Mensajes---#
MENSAJE_BIENVENIDA = "Hola! Vamos a determinar cual numero es mayor al otro"

#---Entrada Codigo---#
print (MENSAJE_BIENVENIDA)
numeroA = int (input(P_numeroA))
numeroB = int (input(P_numeroB))
Amayor = numeroA > numeroB
#---Condicionales---#
if (numeroA > numeroB):
    print (f"El numero A es mayor que B, pues {numeroA} > {numeroB}")
elif (numeroB > numeroA):
    print (f"El numero B es mayor que A, pues {numeroB} > {numeroA}")
else:
    print (f"El numero A es igual a B, pues {numeroA} = {numeroB}")

