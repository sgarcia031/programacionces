# Calcular en que rango se encuentran los niveles de trigliceridos y de homocisteina en un paciente
#---MENSAJES---#
MENSAJE_BIENVENIDA = "Hola! primero determinaré en que rango se encuentran los niveles de trigliceridos..."
MENSAJE_HEMOCISTEINA = "Ahora determinaré el rango de la Homocisteina..."
MENSAJE_N_OPTIMO_T = "Excelente, los niveles de trigliceridos son optimos"
MENSAJE_N_lIMITE_T = "Cuidado, los niveles de trigliceridos sobrepasan ligeramente el limite optimo"
MENSAJE_N_ALTO_T = "Los niveles de trigliceridos son altos, debe cuidar su salud"
MENSAJE_N_MUY_ALTO_T = "Debe ponerse manos a la obra, los niveles de trigliceridos son muy altos, pueden tener repercuciones negativas para la salud"

MENSAJE_N_OPTIMO_H = "Excelente, el nivel de Homocisteina es optimo"
MENSAJE_N_lIMITE_H = "Cuidado, el nivel de Homocisteina sobrepasa ligeramente el limite optimo"
MENSAJE_N_ALTO_H = "El nivel de Homocisteina es alto, debe cuidar su salud"
MENSAJE_N_MUY_ALTO_H = "Debe ponerse manos a la obra, el nivel de Homosisteina es muy alto, puede tener repercuciones negativas para la salud"
#---PREGUNTAS---#
pregunta_trig = "Por favor ingrese niveles de trigliceridos del paciente en mg/dl: "
pregunta_homo = "Ingrese ahora el nivel de Homocisteina del paciente en micromoles/L: "
#---Entrada Trigliceridos---#
print (MENSAJE_BIENVENIDA)
trigliceridos = float (input (pregunta_trig))
if (trigliceridos < 150):
    print (MENSAJE_N_OPTIMO_T)
elif (trigliceridos >= 150 and trigliceridos < 200):
    print (MENSAJE_N_lIMITE_T)
elif (trigliceridos >= 200 and trigliceridos < 500):
    print (MENSAJE_N_ALTO_T)
else:
    print (MENSAJE_N_MUY_ALTO_T)
#---Entrada Homocisteina---#
homocisteina = float (input (pregunta_homo))
if (homocisteina >= 2 and homocisteina < 15):
    print (MENSAJE_N_OPTIMO_H)
elif (homocisteina >= 15 and homocisteina < 30):
    print (MENSAJE_N_lIMITE_H)
elif (homocisteina >= 30 and homocisteina < 101):
    print (MENSAJE_N_ALTO_H)
else:
    print (MENSAJE_N_MUY_ALTO_H)
