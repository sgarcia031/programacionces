import matplotlib.pyplot as plt
#Punto 1
ingresosMesAMes = [2.1, 2, 1.7, 1.4, 2.2, 2, 2.5, 1.9, 2.7, 2.4, 2.1, 2.2]
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiempre','Octubre','Noviembre','Diciembre']

plt.bar(meses, ingresosMesAMes, width=0.7, color= 'b')

plt.title ('Ingresos mensuales durante el Año 2020')
plt.xlabel('Meses')
plt.ylabel('Ingresos (Millones de Pesos)')

plt.savefig('graficoBarrasTaller.png')
plt.show()

#2 Punto 
ciudades = ['Medellin', 'Barranquilla', 'Cali', 'Bucaramanga', 'Cartagena']
habitantes = [2.57, 1.206, 2.23, 0.58, 0.91]
pieExplode = [0.1,0,0,0,0]

acumulado = 0 
for i in range (len(ciudades)):
    ciudades[i] += '-->' + str(habitantes[i])+ ' Millones'

plt.title('Poblacion de habitantes en ciudades de Colombia')
plt.pie (habitantes, explode=pieExplode, labels=ciudades, shadow=True)
plt.savefig('TallerTorta.png')
plt.show()

#Punto 3
import pandas as pd
ppgData = pd.read_csv('ppg.csv', encoding='UTF-8', header= 0, delimiter=';').to_dict()

print(ppgData.keys())
muestras = list(ppgData['muestra'].values())
print(muestras)
valores = list(ppgData['valor'].values())

plt.plot(muestras, valores)
plt.xlabel('Milisegundos')
plt.ylabel('Milivoltios(vM)')
plt.savefig('ppgTaller.png')
plt.show()

