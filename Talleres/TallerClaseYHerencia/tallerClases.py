#Punto 1
class Torta ():
    def __init__(self, formaTorta, saborTorta, alturaTorta):
        self.forma = formaTorta
        self.sabor = saborTorta
        self.altura = alturaTorta
    def mostrarAtributos (self):
        print (f'Esta torta tiene una forma {self.forma}, sabe a {self.sabor} y su altura es de {self.altura} cm')

tortaChocolate = Torta ('circular', 'chocolate', 15)
tortaChocolate.mostrarAtributos()

#Punto 2
class Estudiante ():
    def __init__(self, edadPersona, nombrePersona, idPersona, carreraCursada, semestreCursado):
        self.edad = edadPersona
        self.nombre = nombrePersona
        self.id = idPersona
        self.carrera = carreraCursada
        self.semestre = semestreCursado
    def tiempoEstudio (self, materiaEstudiada, tiempoMateria):
        print (f'Hola, me llamo {self.nombre} y voy a estudiar {materiaEstudiada} por {tiempoMateria} horas')

estudiante = Estudiante (18, 'Samuel', 100137290, 'Ingenieria Biomedica', 2)
estudiante.tiempoEstudio ('Programacion', 3)

#Punto 3
class Nutricionista ():
    def __init__(self, edadN, nombreN, universidadEgresada):
        self.edad = edadN
        self.nombre = nombreN
        self.universidad = universidadEgresada
    
    def calcularIMC (self, pesoIn, alturaIn):
        imc = round (pesoIn/(alturaIn)**2, 4)
        print (f'El IMC de esta persona es {imc}')
    
nutricionista = Nutricionista (23, 'Jessica', 'CES')
nutricionista.calcularIMC (68, 1.75)

#Punto 4
class Canguro ():
    def __init__(self, edadIn, idIn, nombreIn):
        self.edad = edadIn
        self.id = idIn
        self.nombre = nombreIn
    def saltos (self, cantidadSaltos):
        for i in range (cantidadSaltos):
            print (f'{self.nombre} acaba de dar {i+1} saltos')

canguro = Canguro (17, 34224423, 'Esteban')
canguro.saltos(7)

#Punto 5
class Instrumento ():
    def __init__(self, instrumento, entonacion):
        self.instrumento = instrumento
        self.entonacion = entonacion

    def sonar (self, cancion):
        print(f'Tititititi tin tin tiii tonnn...')

piano = Instrumento ('piano', 'aguda')
piano.sonar ("Fur elise")

