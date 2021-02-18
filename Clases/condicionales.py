#---Constantes---#
MENSAJE_BIENVENIDA = "Hola! Espero que estes muy bien..."
PREGUNTA_NUMERO_A = "Ingrese numero A : "
PREGUNTA_NUMERO_B = "Ingrese numero B : "
MENSAJE_MAYOR = "El numero A es mayor que B"
MENSAJE_MENOR = "El numero A es menor que B"
MENSAJE_IGUAL = "A y B son iguales"
#---Entrada al c'odigo---#
print (MENSAJE_BIENVENIDA)
numeroA = int (input(PREGUNTA_NUMERO_A))
numeroB = int (input(PREGUNTA_NUMERO_B))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB
resultado = ""
if (isMayor):
    resultado = MENSAJE_MAYOR
    print (MENSAJE_MAYOR)
elif (isMenor):
    resultado = MENSAJE_MENOR
    print (MENSAJE_MENOR) 
else:
    resultado = MENSAJE_IGUAL
    print (MENSAJE_IGUAL)

print (resultado)
