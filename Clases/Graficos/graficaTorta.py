import matplotlib.pyplot as plt
pielabels = ['Python', 'Java', 'Dart', 'Js']    #Lables: Python, java, dart, js --> Determinan el orden
sizes = [50, 25, 15, 10]    #Sizes son los tamaños de cada porcion de la torta, automaticamente cambia colores
pieExplode = [0, 0, 0.1, 0] #Explode --> Que tan alejado del origen esta la torta. 10% = 0.1. Son para resaltar

##########
def etiquetarElementosPorcentuales (sizes, labels, indicador = '-->'):
    acumulado = 0
    for elemento in sizes:
        acumulado += elemento

    for i in range (len(pielabels)):
        pielabels[i] += indicador + str(sizes[i]/acumulado*100) + '%'

etiquetarElementosPorcentuales(sizes, pielabels, '=')

plt.pie (sizes, explode=pieExplode, labels=pielabels, shadow=True, startangle=45) #lables = marcadores; startangle= angulo de inclinacion de donde empieza el origen
########
plt.title ('Uso de lenguajes de programacion en el 2021')
plt.savefig ('tortaslenguajes.png')
########
plt.show() #El grafico se hace en sentido antihorario