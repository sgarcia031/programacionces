import matplotlib.pyplot as plt
#Punto 1
mensaje_bienvenida = 'Hola, por favor ingresa tus 5 snacks favoritos:'
mensaje_precios = 'Ahora ingresa el precio (en pesos) de cada snack que ingresaste respectivamente:'
listaSnacks = []
listaPrecios = []
print(mensaje_bienvenida)
for i in range (5):
    ingresoSnacks = input()
    listaSnacks.append (ingresoSnacks)

print (f'Excelente! la lista de los snacks es: {listaSnacks}')
print(mensaje_precios)
for i in range (5):
    ingresoPrecios = float(input())
    listaPrecios.append(ingresoPrecios)

plt.bar(listaSnacks, listaPrecios, width=0.6, color= 'c')
plt.title ('Snacks favoritos con sus respectivos precios')
plt.xlabel ('Snacks')
plt.ylabel ('Precio por unidad')
plt.savefig('barrasquiz.png')
plt.show()

#Punto 2
mensaje_ciudades = 'Bienvenido, por favor ingresa tus 5 ciudades favoritas en el mundo:'
mensaje_poblaciones = 'Ahora ingresa la poblacion de cada una de estas ciudades (en millones) de una forma respectiva:'
listaCiudades = []
listaPoblaciones = []
print(mensaje_ciudades)
for i in range (5):
    ingresoCiudades = input()
    listaCiudades.append (ingresoCiudades)
print(f'Perfecto! La lista de las ciudades es: {listaCiudades}')
print (mensaje_poblaciones)
for i in range (5):
    ingresoPoblaciones = float(input())
    listaPoblaciones.append (ingresoPoblaciones)

for i in range (len(listaCiudades)):
    listaCiudades[i] += '-->' + str(listaPoblaciones[i])+ ' Millones'

maximo = max(listaPoblaciones)
mayor = listaPoblaciones.index(maximo)
pieExplode = [0, 0, 0, 0, 0]
pieExplode[mayor] = 0.3
plt.pie(listaPoblaciones, labels= listaCiudades, shadow=True, explode= pieExplode, startangle=45)

plt.title('Poblaciones de ciudades')
plt.savefig('tortaquiz.png')
plt.show()

#Punto 3
import pandas as pd
definicionEcg = 'Los tipos de archivos ECG hacen referencia a las siglas en ingles de "Electrocardiography", archivo el cual reune los datos tomados de un examen de electrocardiograma (el cual mide y reconoce las señales eléctricas generadas en el corazón junto a la frecuenia de los latidos), a continuación se mostrará un ejemplo de este...'
print(definicionEcg)

ecgDatos = pd.read_csv ('ecgQuiz.csv', encoding='UTF-8', header = 0, delimiter= ';').to_dict()
muestrasECG = list(ecgDatos['muestra'].values())
valoresECG = list(ecgDatos['valor'].values())

plt.plot(muestrasECG, valoresECG)
plt.title ('Examen de electrocardiograma')
plt.xlabel ('Tiempo trasncurrido (ms)')
plt.ylabel('Señal eléctrica (mV)')
plt.savefig('exgQuiz.png')
plt.show()
###
definicionPpg = 'El archivo PPG hace referencia a los datos recogidos en un examen de fotopletismografía (que se le da esta extension por las siglas en ingles de "Photoplethylsmography"), la cual es una técnica óptica simple usada para descubrir los cambios volumétricos en sangre durante la circulación, a continuación se verá un ejemplo de los datos recogidos en este examen...'
print(definicionPpg)

ppgDatos = pd.read_csv ('ppgQuiz.csv', encoding= 'UTF-8', header=0, delimiter= ';').to_dict()
muestrasPPG = list(ppgDatos['muestra'].values())
valoresPPG = list(ppgDatos['valor'].values())

plt.plot(muestrasPPG, valoresPPG)
plt.title('Examen de Fotopletismografía')
plt.xlabel('Tiempo transcurrido (s)')
plt.ylabel('Señales eléctrica (mV)')

plt.savefig('ppgQuiz.png')
plt.show()









