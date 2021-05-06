import matplotlib.pyplot as plt  #Matplotlib es una libreria completa, con el .pyplot se trae una parte de sus funcionalidades
lenguajes = ['python', 'java', 'ts', 'elixir']  #Eje x/ Datos
encuesta = [50, 10, 20 ,10]  #Altura
plt.bar(lenguajes, encuesta, width = 0.9, color = 'r' ) #Width por defecto es 0.8, si pongo 1 estarian pegados 
#####
plt.title ('Lenguajes mas usados')  #Titulo
#####
plt.xlabel ('Lenguajes programacion')  #Etiqueta del eje X
#####
plt.ylabel ('Porcentaje de uso de lenguajes')   #Etiqueta del eje Y
#####
plt.savefig ('graficoLenguajes.png')   #Guardar el grafico en el computador con ese nombre
#####
plt.show()