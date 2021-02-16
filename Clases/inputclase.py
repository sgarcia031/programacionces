#-----Constantes------#
PREGUNTA_NOMBRE = "Como te llamas? : "
MENSAJE_SALUDO = "Un gusto conocerte"
PREGUNTA_EDAD = "Cuantos años tienes? : "
PREGUNTA_ESTATURA = "Cuanto mides? : "
#----Entrada al codigo----#
nombre = input (PREGUNTA_NOMBRE)
edad = int (input (PREGUNTA_EDAD))
print (nombre, MENSAJE_SALUDO)
print (f"En ocho años tendras {edad + 8} años")
estatura = float (input(PREGUNTA_ESTATURA))
print (estatura)

