class Humano():
    '''
    Esta es la clase Humano, exige atributos.
    nombreEntrada: Hace referencia al nombre de usuario.
    edadEntrada: Hace referencia a la edad del usuario.

    Tiene las siguientes acciones:

    *hablar(mensaje):
        Dado un mensaje, lo muestra en pantalla
    *mostarAtributos:
        Dado 

    '''
    def _init_ (self, nombreEntrada, edadEntrada, estaturaEntrada) :     # Estos son los atributos
        print('Hola, soy un humano nuevo')
        self.edad = edadEntrada
        self.raza = 'Humano'
        self.nomnbre = nombreEntrada
        self.estatura = estaturaEntrada
        self.dinero = 

    def hablar (self, mensaje):
        print(f'Hola, soy {self.nombre} tengo un mensaje que decir')                        #def de accion, self --> guarda atributos 

    def mostrarAtributos(self):
        print (f'''Mi nombre es {self.nombre}
                    Mi estatura es {self.estatura} metros
                    Mi edad es {self.edad} años
                    Tengo ahorrado {self.dinero}''')

    def recorrerDistancia (self, distanciaMetros):
        for i in range (distanciaMetros):
            print(f'Hola, soy {self.nombre} y he recorrido {i+1} metros')
    
    def ahorrarDinero (self):
        preguntaIngresarMontos ='Ingrese S --> para continuar añadiendo montos y N--> para finalizar'
        preguntaMonto= 'Cuanto vas a ingresar?'
        ingresarMontos = input(preguntaIngresarMontos)
        while (ingresarMontos != 'N'):
            monto = float (input(preguntaMonto))
            self.dinero = self.dinero + monto
            ingresarMontos = input(preguntaIngresarMontos)
            print(f'Soy {self.nombre} y tengo {self.dinero}')
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
totalAhorrado = humano2.ahorrarDinero()
print(totalAhorrado)
humano2.mostrarAtributos()
