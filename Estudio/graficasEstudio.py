import matplotlib.pyplot as plt
musculos = ['Pecho', 'bicep', 'tricep', 'Espalda', 'Pierna']
tamaños = [20, 10, 10, 15, 13]
resaltar = [0, 0, 0, 0, 0.3]

plt.pie(tamaños, explode=resaltar, labels= musculos, shadow=True)

plt.show()