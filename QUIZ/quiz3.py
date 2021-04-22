#Integrantes: Samuel Garcia Isaza, Cristian Bustamante
class Elementosdigitales ():
    def __init__(self, nombreCancion ,creadorEntrada ,fechaDePublicacion):
        self.nombre = nombreCancion
        self.creador = creadorEntrada
        self.fecha = fechaDePublicacion
    def mostrarAtributos (self):
        print (f'''El nombre de la cancion es "{self.nombre}" 
                    Del artista llamado {self.creador}
                    Fue lanzada el {self.fecha}''')

class Usuario ():
    def __init__(self, nombreIn, edadIn, sexoIn, nacionalidadIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.sexo = sexoIn
        self.nacionalidad = nacionalidadIn
    def mostrarAtributos (self):
        print (f'''El usuario es llamado {self.nombre} 
                    Tiene una edad de {self.edad} años
                    Es de sexo {self.sexo}
                    Tiene nacionalidad {self.nacionalidad}''')
    def escuchandoCancion (self, cancionEscuchada):
        print(f'Hola, soy {self.nombre} y estoy escuchado {cancionEscuchada}')

class Pagina ():
    def __init__(self, tipoDeContenido, formato, fechaPublicacion):
        self.tipoContenido = tipoDeContenido
        self.formato = formato
        self.fecha = fechaPublicacion
    def mostrarAtributos (self):
        print (f'''Esta pagina tiene un contenido centrado en {self.tipoContenido}
                    Se encuentra en un formato {self.formato}
                    Su fecha de publicacion fue el {self.fecha}''')

#Herencia
class Cancion (Elementosdigitales):
    def __init__(self, nombreCancion, creadorEntrada, fechadepublicacion, generomusical, duracionCancion):
        Elementosdigitales.__init__(self, nombreCancion,creadorEntrada,fechadepublicacion)
        self.generomusical = generomusical
        self.duracion = duracionCancion 
    def cancionCreada (self):
        print (f'La cancion {self.nombre} acaba de ser añadida, su fecha de publicacion es el {self.fecha}')
    def bucle (self, cantidadVeces):
        for i in range (cantidadVeces):
            print (f'La cancion {self.nombre} acaba de sonar por {i+1} vez')

class Artista (Usuario):
    def __init__(self, nombreIn, edadIn, sexoIn, nacionalidadIn, generoMusical, numeroCanciones, numeroAlbums):
        Usuario.__init__(self, nombreIn, edadIn, sexoIn, nacionalidadIn)
        self.genero = generoMusical
        self.canciones = numeroCanciones
        self.albums = numeroAlbums
    def concierto (self, ciudadVisitada):
        print (f"Soy {self.nombre}, esten muy atentos ya que visitare {ciudadVisitada} para hacer un concierto")

listaFavoritos = []
class Favoritos (Pagina):
    def __init__(self, tipoDeContenido, formato, fechaPublicacion, favoritosComunidad, fechaUltimaActualizacion):
        Pagina.__init__(self, tipoDeContenido, formato, fechaPublicacion)
        self.favoritos = favoritosComunidad
        self.actualizacion = fechaUltimaActualizacion
    
    def añadirCancion (self, cancionAñadida, actualizacion):
        listaFavoritos.append(cancionAñadida)
        self.actualizacion = actualizacion
        print (f'Lista de favoritos: {listaFavoritos}, ultima actualizacion: {actualizacion}') 
    def eliminarCancion (self):
        preguntaEliminar = int (input ('Ingrese el numero de la lista de favoritos que desea eliminar: '))
        listaFavoritos.pop (preguntaEliminar - 1)
        print (f'Ahora la lista de favoritos es: {listaFavoritos}')

print ('-'*50)
trescanciones = Cancion("TresCanciones", "Diomedes Diaz", "24 de diciembre de 1987", 'Vallenato', '3 minutos con 10 seg')
trescanciones.mostrarAtributos()
trescanciones.cancionCreada ()
trescanciones.bucle (4)

print ('-'*50)
bachata = Favoritos("Bachata", "MP3", "14 de Febrero del 2020", listaFavoritos, "enero 2021")
bachata.mostrarAtributos()
bachata.añadirCancion ('Obsesion', '10 de abril')
bachata.añadirCancion ('Flor palida', '12 de abril')
bachata.añadirCancion ('Odio', '22 de abril')
bachata.eliminarCancion ()

print ('-'*50)
cantante = Artista ('Bad bunny', 23, 'Masculino', 'Puerto Riqueña', 'Trap', 156, 15)
cantante.mostrarAtributos()
cantante.concierto ('Bogota')
cantante.escuchandoCancion ('Te bote')

