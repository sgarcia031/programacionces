#---MENSAJES---#
MENSAJE_BIENVENIDA = "Hola! podre convertir una medida dada en cm a cualquier otra medida..."
MENSAJE_VALOR = "Ingrese el valor que desee convertir en cm: "
MENSAJE_MEDIDAS = """km - Kilometros
M - Metros
mm - Milimetros
Ingrese ahora a que unidad desea transformar: """

MENSAJE_ERROR = "Entrada no valida, por favor ingrese una unidad entre las opciones"
#---ENTRADA CODIGO---#
print (MENSAJE_BIENVENIDA)
medida = float (input(MENSAJE_VALOR))
unidad = input(MENSAJE_MEDIDAS)
#---Conversiones---#
metros = medida*10**-2
kilometros = medida*10**-5
milimetros = medida*10
#---Condicionales---#
if (unidad == "km"):
    print (f"la respuesta de pasar {medida} cm a {unidad} es: {kilometros} Km")
elif (unidad == "M"):
    print (f"la respuesta de pasar {medida} cm a {unidad} es: {metros} M")
elif (unidad == "mm"):
    print (f"la respuesta de pasar {medida} cm a {unidad} es: {milimetros} mm")
else:
    print (MENSAJE_ERROR)
