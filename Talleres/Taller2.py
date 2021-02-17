#---Constantes---#
MENSAJE_BIENVENIDA = "Hola! haré algunos calculos con dos valores dados..."
INGRESAR_N_A = "Ingresa un valor entero : "
INGRESAR_N_B = "Excelente! Ahora ingresa otro valor : "
VERIFICAR_IGUALES = "Ahora vamos a verificar si estos numeros son iguales"
MENSAJE_DESPEDIDA = "Muchas gracias por participar!"
PREGUNTA_MAYOR = "El primer valor es mayor al segundo?"
#---Entrada de codigo---#
print (MENSAJE_BIENVENIDA)
valorA = int (input (INGRESAR_N_A))
valorB = int (input (INGRESAR_N_B))
print (f"La suma de estos valores da el resultado de {valorA + valorB}")
print (f"El resultado de restar el primer valor con el segundo es {valorA - valorB}")
print (f"Si multiplicamos ambos valores el resultado sería {valorA * valorB}")
print (f"El primer valor elevado al segundo tendria como respuesta {valorA ** valorB}")
print (f"Si dividimos el primer valor entre el segundo el resultado sería {valorA / valorB}")
print ("-"*10, (PREGUNTA_MAYOR), "-"*10)
isMayor = valorA > valorB
print ("La respuesta es", isMayor)
print ("-"*10, (VERIFICAR_IGUALES), "-"*10)
dividir = valorA / valorB
isIgual = dividir == 1
print ("El resultado de que estos valores sean iguales es", isIgual)
print (MENSAJE_DESPEDIDA)