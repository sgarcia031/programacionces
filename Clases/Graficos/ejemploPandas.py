import matplotlib.pyplot as plt
import pandas as pd
ecgData = pd.read_csv('ecg.csv',encoding='UTF-8', header=0, delimiter=';').to_dict() #to_dict = funcion que dice mandemelo a diccionario
#Encoding (formato) = UTF-8 (universal text format) Para detectar lenguaje universal (con tildes, etc) enves de ser un formato ingles
#Header = le dice a pandas posicion ('coordenada')en donde se ecuentra el titulo, este caso seria un 0 porque esta en la posicion 1

print(ecgData.keys()) #.keys son las llaves del diccionario para obtener los valores de cada coordenada (posicion) --> encabezado
muestras = list(ecgData['muestra'].values()) #Es una lista que viene de ecgData en la llave (encabezado) 'muestra'.values (para traerme los valores)
print(muestras) #unicamente los valores del encabezado 'muestra'
valores = list(ecgData['valor'].values())
print(valores[-10:]) #mostrar las ultimas 10 posiciones (desde -10 hasta terminar)
########
plt.plot(muestras, valores) # x contra y
plt.show()