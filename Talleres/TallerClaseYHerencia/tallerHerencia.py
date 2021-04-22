#Punto 1
class Persona ():
    def __init__(self, idPersona, nombrePersona, edadPersona):
        self.id = idPersona
        self.nombre = nombrePersona
        self.edad = edadPersona
    def caminar (self, cantidadMetros):
        for i in range (cantidadMetros):
            print (f'Hola, soy {self.nombre} y acabo de caminar {i+1} metros')
        print (f'En total camine {cantidadMetros} metros')

personaX = Persona (22398, 'Jacobo', 25)
personaX.caminar (10)

#Punto 2
class Doctor (Persona):
    def __init__(self, idPersona, nombrePersona, edadPersona, especialidadIn):
        Persona.__init__(self, idPersona, nombrePersona, edadPersona)
        self.especialidad = especialidadIn
    def tratamiento (self, enfermedad):
        print (f'Hola, me llamo {self.nombre} y soy un {self.especialidad}, procedo a tratar la enfermedad {enfermedad}')

internista = Doctor(2492, 'Alex', 30, 'internista')
internista.tratamiento('Diabetes')

#Punto 3
class Nutricionista (Persona):
    def __init__(self, idPersona, nombrePersona, edadPersona, universidadEgresada):
        Persona.__init__(self, idPersona, nombrePersona, edadPersona)
        self.universidad = universidadEgresada
    def calcularIMC (self, altura, peso):
        imc = (round (peso/(altura)**2, 2))
        print (f'Hola, me llamo {self.nombre} y el IMC calculado de esta persona es {imc}')

nutricionistaX = Nutricionista (3423524, 'Sofia', 24, 'UPB')
nutricionistaX.calcularIMC (1.72, 80)

#Punto 4
class Abogado (Persona):
    def __init__(self, idPersona, nombrePersona, edadPersona, especialidadIn, universidadEgresado):
        Persona.__init__(self, idPersona, nombrePersona, edadPersona)
        self.especialidad = especialidadIn
        self.universidad = universidadEgresado
    def representante (self, nombreRepresentado, casoCliente):
        print (f'Buenos dias, mi nombre es {self.nombre}, procedo a representar al cliente {nombreRepresentado} en el caso de {casoCliente}...')

audiencia = Abogado (1232421, 'Javier', 40, 'Derecho Familiar', 'Eafit')
audiencia.representante('Miguel', 'Divorcio')