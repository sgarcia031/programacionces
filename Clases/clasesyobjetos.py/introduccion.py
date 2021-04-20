class Humano():
    '''
    Esta es la clase Humano, exige atributos.
    nombreEntrada: Hace referencia al nombre de usuario.
    edadEntrada: Hace referencia a la edad del usuario.
    estaturaEntrada: Hace referencia a la estatura del usuario.

    Tiene las siguientes acciones:

    *hablar(mensaje):
        Dado un mensaje, lo muestra en pantalla
    *mostarAtributos():
        Muestra los atributos del usuario.
    '''
    def __init__ (self, nombreEntrada, edadEntrada, estaturaEntrada) :     # Una funcion dentro de unas clase es una ACCION
        print('Hola, soy un humano nuevo')                              #init es la funcion inicial, esta accion se va a ejecutar SIEMPRE al crear un nuevo objeto
        self.edad = edadEntrada                                         #Self es una "cajita" donde se van a guardar todos sus atributos
        self.raza = 'Humano'
        self.nombre = nombreEntrada
        self.estatura = estaturaEntrada
        self.dinero = 0

    def hablar (self, mensaje):
        print(f'Hola, soy {self.nombre} tengo un mensaje que decir')                        #def de accion, self --> guarda atributos 

    def mostrarAtributos(self):
        print (f'''Mi nombre es {self.nombre}
                    Mi estatura es {self.estatura} metros
                    Mi edad es {self.edad} años
                    Tengo ahorrado {self.dinero}''')

    def recorrerDistancia (self, distanciaMetros):
        for i in range (distanciaMetros):
            print(f'Hola, soy {self.nombre} y he recorrido {i+1} metros')  #Ya que i arranca en cero
    
    def ahorrarDinero (self):
        preguntaIngresarMontos ='Ingrese S --> para continuar añadiendo montos y N--> para finalizar:  '
        preguntaMonto= 'Cuanto vas a ingresar?: '
        ingresarMontos = input(preguntaIngresarMontos)
        while (ingresarMontos != 'N'):
            monto = float (input(preguntaMonto))  #Le va a preguntar a la persona por el monto
            self.dinero = self.dinero + monto      #Modificar lo que hay en self.dinero (0), sumandole lo que ahorro
            ingresarMontos = input(preguntaIngresarMontos)          #Preguntar si quiere ingresar un monto nuevamente, sino se quedaria infinito
            print(f'{self.nombre}, tienes {self.dinero} pesos ahorrados')
        return self.dinero

humano1 = Humano('Daniel', 27, 1.67)
humano2 = Humano('Mafer', 27, 1.60)

humano1.hablar('Espero que esten muy bien')
humano2.hablar('Chao')

print (humano1.nombre)
print (humano2.nombre)
print (humano1.edad)

humano1.mostrarAtributos()
humano2.mostrarAtributos()
humano1.recorrerDistancia (25)
#Si la funcion tiene solo un return, pero no se muestra, por ello:...
totalAhorrado = humano2.ahorrarDinero()
print(f'En total tienes {totalAhorrado} pesos ahorrados')

class Ingeniero(Humano):
    def __init__(self, nombreEntrada, edadEntrada, estaturaEntrada, areaEntrada):
        Humano.__init__ (self, nombreEntrada, edadEntrada, estaturaEntrada)
        self.area = areaEntrada 
    def solucionarProblemas (self, problema):
        print (f'Hola, soy un ingeniero y me llamo {self.nombre} y proceso a solucionar el problema {problema}')

class Programador (Humano):
    def crearAlgoritmo (self, algoritmo):
        print (f'Hola, son un programador y procedo a resolver el algoritmo {algoritmo}')

class Biomedico (Ingeniero, Programador):    #Clase de biomedico que hereda de ingeniero y programador, el cual heredan de Humano
    def mantenimientoEquiposMedicos (self, nombreEquipo):
        print (f'Hola soy {self.nombre} y precedo a arreglar el {nombreEquipo}')

biomedico = Biomedico ('Karla', 20, 1.63, "Biomedicina")
biomedico.recorrerDistancia (25)
biomedico.mostrarAtributos()
biomedico.mantenimientoEquiposMedicos ('Electrocardiograma')
biomedico.crearAlgoritmo ('Fibonacci')
biomedico.solucionarProblemas ('Ocupacion alta de UCIs')
print (biomedico.area)

class Abogado (Humano):
    def levantarAccionDeTutela (self, nombreCliente):
        print (f'Hola Soy {self.nombre} y estoy representando a {nombreCliente}')
abogado1 = Abogado ('Stiven', 34, 1.80)

abogado1.mostrarAtributos ()
abogado1.levantarAccionDeTutela(biomedico.nombre)    #Traer nombre de karla