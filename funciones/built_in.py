import math
#BUILT IN son funciones que ya existen dentro del lenguaje

#PRINT es una funcion que muestra por pantalla(terminal o linea de comandos ) el argumento entregado
print ('Este es el ARGUMENTO  de la funcion')

#el metodo (o funcion) ROUND redondea un numero a una cantidad especifica de decimales
print(round(math.pi, 3))

lista_numeros = [10,20,30,40,50]
#el metodo SUM suma los elementos de una lista entregados como argumentos
print(sum(lista_numeros))
print(sum([1,5,7,17,9]))

#el metodo INPUT permite al usuario ingresar datos que SIEMPRE seran de tipo string
nombre = input('ingrese su nombre: ')
print(nombre) 