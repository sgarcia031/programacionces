
preguntaGenero = input ('Que genero de tigre acabas de ver, un macho o una hembra? (ingrese solo macho o hembra): ')
class Tigre ():
    def __init__ (self, genero, nombreEntrada):
        print (f'Acabas de avistar a un tigre {preguntaGenero}')
        if (preguntaGenero == 'hembra'):
            entradaPeso = 'Entre 65 - 170kg'
            entradaLongitud = '2 - 2.8 metros'
        elif (preguntaGenero == 'macho'):
            entradaPeso = '90 - 310kg'
            entradaLongitud = '2.5 - 3.9 metros'
        else:
            print ('Entrada no valida')
        self.nombre = nombreEntrada
        self.longitud = entradaLongitud
        self.peso = entradaPeso
        self.pelaje = 'lineas negras con un fondo anaranjado rojizo o blanco'
        self.alimento = 'son fundamentalmente carnívoros: comen ciervos, venados, cerdos salvajes , búfalos y en general, no desperdician la oportunidad de cazar una presa pequeña.'
        self.claseAnimal = 'Felinos'
        self.tiempoDeVida = '8-10 años'

    def mostrarCaracteristicas (self):
        print (f'''Este tigre se llama {self.nombre}. Al ser {preguntaGenero} puede tener una longitud de {self.longitud}. 
                    Su peso oscila entre {self.peso}.
                    Se caracterizan por tener un pelaje de {self.pelaje}.
                    Pertenece a la clase animal de los {self.claseAnimal}''')

    def comer (self, animalAlimento):
        print (f'El tigre se acaba de comerse a un(a) {animalAlimento}, esto debido a que {self.alimento}')

    def edad (self):
        preguntaEdad = 'Cuantos años tiene aproximadamente: '
        ingresoEdad = int(input (preguntaEdad))
        if (ingresoEdad > 10):
            print (f'Esto no puede ser cierto, puesto a que los tigres viven en promedio de {self.tiempoDeVida}')
        elif (ingresoEdad <= 10):
            print (f'Es posible que tenga esa edad, puesto a que los tigres viven en promedio de {self.tiempoDeVida}')
        else: 
            print ('Entrada no valida')

class Bengala (Tigre):
    def ubicacion (self, lugar):
        print (f'Puede ser encontrado en {lugar}')

bengala = Bengala (preguntaGenero, 'Pepito')
bengala.mostrarCaracteristicas()
bengala.ubicacion ('India')

class Siberiano (Bengala):
    def colorPelaje (self, color):
        print (f'tiene pelaje color {color}')


siberiano = Siberiano (preguntaGenero, 'Piter Albeiro')
siberiano.mostrarCaracteristicas()
siberiano.colorPelaje ('Blanco')
siberiano.ubicacion ('Antartida')


tigreVisto = Tigre(preguntaGenero, 'Alex')

tigreVisto.mostrarCaracteristicas()
tigreVisto.comer('Gato')
tigreVisto.edad()
