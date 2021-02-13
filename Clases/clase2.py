pruebaV=True
pruebaF=False

print (pruebaV)
print (pruebaF)

edad = 18
estatura = 1.74
peso = 70
NOMBRE = "Samuel Garcia Isaza"
print ("#"*15, "Mayor Edad", "#"*15)
isMayorEdad = edad >= 18
print (isMayorEdad)
print ("-"*15, "bajo la estatura promedio", "-"*15)
isMayorEstatura = estatura < 1.70
print (isMayorEstatura)
# calculando si el peso es diferente de 84
print ("#"*15, "peso diferente de 84", "#"*15)
isPesoDiferente = peso != 84
print (isPesoDiferente)
# Vamos a ver si un apellido esta en el nombre completo
apellido = "garcia"
isApellido = apellido in NOMBRE
print ("#"*15, "Esta apellido en el nombre?", "#"*15)
print (isApellido)
