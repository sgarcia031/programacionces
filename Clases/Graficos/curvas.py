import matplotlib.pyplot as plt
tiempo = [0, 1, 2, 3, 4, 5]
sensor = [4,5,6,7,9,9]

plt.plot(tiempo, sensor, '--,c')
######
plt.title ('Grafico del sensor contra el tiempo')
plt.xlabel ('Tiempo (s)')
plt.xlabel('Voltaje (mV)')
plt.savefig('graficoSensor.png')

######
plt.show()
#########



diccionario['NombresEstudiantes'] = ['Jacobo', 'Dani', 'Maria', 'Elena']
diccionario['EdadEstudiantes'] = [18, 22, 32, 14]
diccionario['Peso'] = [84,56,60,57]
print(diccionario)

print(diccionario['NomresEstudiantes'][-1], diccionario['EdadEstudiantes'][-1], diccionario['Peso'][-1])  #Mostrar todo eso, -1 = ultimo dato de lista