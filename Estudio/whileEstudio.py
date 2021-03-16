# #1. Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
MENSAJE_NUMERO = "Por favor ingrese un numero cualquiera, en caso de querer salir para mostrar el resultado de la sumatoria, ingrese 0: "
MENSAJE_SALIDA = "Muchas gracias por participar"
#--Entrada--#
pregunta_numero = int (input(MENSAJE_NUMERO))
sumatoria = 0
while (pregunta_numero != 0):
    sumatoria += pregunta_numero
    pregunta_numero = int (input(MENSAJE_NUMERO))
print (f'La sumatoria de los numeros ingresados es {sumatoria}')
print (MENSAJE_SALIDA)

# #2. Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero. El programa terminará
pregunta_numero_A = 'Por favor ingrese un valor cualquiera: '
pregunta_numero_B = 'Por favor ingrese un segundo valor que sea mayor al primero: '
MENSAJE_ERROR = 'Recuerda que debes ingresas un valor que sea mayor al primero'
#--Entrada--#
ingresar_numeroA = int(input(pregunta_numero_A))
ingresar_numeroB = int(input(pregunta_numero_B))
while (ingresar_numeroB < ingresar_numeroA):
    print (MENSAJE_ERROR)
    ingresar_numeroB = int(input(pregunta_numero_B))

print ('Muchas gracias, efectivamente el segundo valor es mayor al primero')

#3. Escriba un programa que pida números enteros mientras sean cada vez más grandes.
pregunta_N_A = 'Por favor ingrese un numero entero: '
pregunta_N_B = 'Ahora ingrese un numero mayor al anterior: '
mensaje_Entrada = "Debes ingresar un numero mayor al anterior para continuar con el juego, en caso de querer acabarlo ingresa 0"
print(mensaje_Entrada)
ingreso_N_A = int (input(pregunta_N_A))
ingreso_N_B = int (input(pregunta_N_B))

while (ingreso_N_A < ingreso_N_B and ingreso_N_A != 0 and ingreso_N_B != 0):
    print(f'El numero {ingreso_N_B} es mayor a {ingreso_N_A}, puedes proseguir correctamente')
    ingreso_N_A = ingreso_N_B
    ingreso_N_B = int (input(pregunta_N_B))
while (ingreso_N_A > ingreso_N_B and ingreso_N_B != 0):
    print (f'Recuerda que debes poner un numero mayor a {ingreso_N_A}')
    ingreso_N_B = int (input(pregunta_N_B))
print('Muchas gracias por participar')

#4. Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
# Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

total = 0
monto = float(input("Monto de venta: $"))
while (monto != 0):
    if (monto<0):
        print ('Valor no valido')
    else:
        total += monto
    monto = float (input("Monto de venta: $"))
if (total > 1000):
    total -= total*0.1
print (f"Monto valor a pagar es: ${total}")




