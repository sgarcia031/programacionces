###PUNTO 1###
import matplotlib.pyplot as plt

mensaje_bienvenida = 'Hola!, por favor escoje e ingresa tus 8 alimentos favoritos, ingresando a su vez el precio que estos tienen...'
lista_alimentos = []
lista_precios = []

for i in range (8):
    ingresoAlimento = input ('Ingresa uno de tus alimentos favoritos: ')
    lista_alimentos.append (ingresoAlimento)
    ingresoPrecio = float (input('Ahora ingresa su precio de mercado: '))
    lista_precios.append (ingresoPrecio)
    print ('-'*20)

plt.bar (lista_alimentos, lista_precios, width = 0.7, color = 'c')

plt.title ('Alimentos favoritos con sus respectivos precios')
plt.xlabel ('Precios de mercado de Alimentos')
plt.ylabel ('Aimentos preferidos')

plt.savefig ('alimentosFav.png')
plt.show()

##PUNTO 2###

class Humano ():
    def __init__(self, nombreIn, sexoIn, edadIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.genero = sexoIn
    
    def hablar (self, mensaje):
        print (f'Hola, me llamo {self.nombre}, y quiero decir que: "{mensaje}"')
    
class Doctor (Humano):
    def calcularIMC (self, estatura, peso):
        imc = peso/(estatura**2)
        print (f'Hola, mi nombre es {self.nombre}, soy doctor y dado los datos puedo decir que el IMC es de {imc}%')

#Probando#
humanoX = Humano('Samuel', 'Masculino', 18)
humanoX.hablar('Me gusta la pizza')

doctorX = Doctor('Jose', 'Masculino', 47)
doctorX.calcularIMC (1.74, 67)

###PUNTO 3###
preguntaNombre = 'Por favor ingrese su nombre: '

isDatoCorrecto = False
while (isDatoCorrecto == False):
    try:
        ingresoNombreUsuario = input (preguntaNombre)
        assert (ingresoNombreUsuario.isalpha())
        isDatoCorrecto = True
    except:
        print ('Dato ingresado no es valido ya que solo debe contener letras...')

isDatoCorrecto = False
while (isDatoCorrecto == False):
    try:
        ingresoDinero = float (input(f'Hola {ingresoNombreUsuario} ¿Cuantos dolares tiene? (ingrese en términos de números): '))
        isDatoCorrecto = True
    except ValueError:
        print ('El valor ingresado no es valido, unicamente puede contener numeros y, en caso de haber decimal, use el punto (.)')

conversion = ingresoDinero*0.82
print (f'Usted cuenta con {conversion} euros')


###PUNTO 4###
import sys
nombreDocumento = 'pacientes.txt'

try: 
    documento = open (nombreDocumento)

except FileNotFoundError:
    documento = open (nombreDocumento, 'w', encoding='UTF-8')
    descripcion = 'En este documento se encontrará el paciente, la enfermedad que presenta y el precio respectivo de cada consulta.'
    documento.writelines(descripcion + '\n' + '-'*30 + '\n')
    print ('El documento no existia, sin embargo, ya ha sido creado existosamente...')
    sys.exit(1)

documento = open (nombreDocumento, 'a')

nombrePaciente = input ('Nombre del paciente: ')
descripcionEnfermedad = input ('Descripcion de enfermedad: ')
precioConsulta = float (input ('Precio de consulta: '))

documento.writelines('Nombre del paciente: ' + nombrePaciente + '\n')
documento.writelines('Descripción de enfermedad: ' + descripcionEnfermedad + '\n')
documento.writelines('Precio de consulta: ' + str (precioConsulta) + '\n')
documento.writelines('-'*30 + '\n')

documento.close()

mensajeProfe = '''Profe muchisimas gracias por todo, sinceramente profesores como usted hay pocos...
                Gracias por acompañarnos, por siempre tener buena actitud y disposicion para atendernos cualquier tipo de duda o solicitud, en general por su buena forma de ser.
                Muchos exitos en el trabajo, mando mis mejores deseos y espero que nos volvamos a encontrar en el futuro.
                Att: Samuel Garcia'''