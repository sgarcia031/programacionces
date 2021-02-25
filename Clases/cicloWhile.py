#---Mensaje---#
MENSAJE_BIENVENIDA = "Bienvenido! Te apoyare ahorrando"
MENSAJE_AHORRO = "Tienes ahorrado..."
#---Pregunta---#
PREGUNTA_VALOR_CPU = "Cuanto vale el PC que deseas?: "
PREGUNTA_CUANTO_TIENE = "Cuanto dinero tienes ahorrado?: "

#---Entrada---#
print (MENSAJE_BIENVENIDA)
valor = float (input(PREGUNTA_VALOR_CPU))
ahorrado = float(input(PREGUNTA_CUANTO_TIENE))

while (valor > ahorrado):
    print (MENSAJE_AHORRO, ahorrado, "Te faltan", valor - ahorrado)
    ahorrado = ahorrado + 1000
print (valor == ahorrado)
