import matplotlib.pyplot as plt
import pandas as pd
ecgData = pd.read_csv('ecg.csv',encoding='UTF-8', header=0, delimiter=';').to_dict() 
#UTF-8 Para detectar lenguaje universal (con tildes, etc) enves de ser un formato ingles
#Header = posicion en donde se ecuentra el titulo, este caso seria un 0 porque esta en la posicion 1

print(ecgData.keys())
muestras = list(ecgData['muestra'].values())
print(muestras)
valores = list(ecgData['valor'].values())
print(valores[-10:]) #mostrar las ultimas 10 posiciones
plt.plot(muestras, valores)
plt.show()