import ejerciciosfunciones as fn

print (fn.sumar(2,4))

print (fn.restar())

print (fn.multiplicar())

print (fn.dividir())

print(fn.potenciar())

print (fn.calcular(fn.potenciar,2,3)) 

#En caso tal de tomar la operacion del mismo archivo
def sumar (a,b):
    return a+b

print (fn.calcular(sumar,2,67))