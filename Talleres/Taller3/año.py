#---preguntas---#
AÑO_ACTUAL = "En que año se encuentra actualmente: "
AÑO_X = "Ahora ingrese un año cualquiera: "
#---Entrada---#
actual = int (input (AÑO_ACTUAL))
cualquiera = int (input (AÑO_X))
#---Condicionales---#
if (actual > cualquiera):
    resta = actual - cualquiera
    print (f"Han pasado {resta} años desde el año {cualquiera}")
elif (cualquiera > actual):
    resta2 = cualquiera - actual
    print (f"Faltan {resta2} años para llegar al año {cualquiera}")
