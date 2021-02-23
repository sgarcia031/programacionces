#---Pregunta---#
PREGUNTA_EDAD = "Ingrese su edad actual: "
#---Mensajes---#
MENSAJE_BIENVENIDA = "Hola, vamos a ver en que rango de edad te encuentras..."
MENOR_EDAD = "Lo siento, no tienes permiso de entrar a bares ya que eres menor de edad"
JOVEN = "Todavia eres muy joven! tienes toda una vida por delante"
ADULTO = "Te estas haciendo viejo! aprovecha tus ultimos años de juventud"
ADULTO_MAYOR = "Ya estas la ultima etapa de tu vida, haz que los dias cuenten!"


#---Entrada---#
print (MENSAJE_BIENVENIDA)
edad = int (input (PREGUNTA_EDAD))
#---Condicionales---#
if (edad < 18):
    print (MENOR_EDAD)
elif (edad >= 18 and edad < 26):
    print (JOVEN)
elif (edad > 25 and edad < 61):
    print (ADULTO)
else:
    print (ADULTO_MAYOR)