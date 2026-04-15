
#solicite al usuario el ingreso de datos personales (nombre, edad, titulo)
#si el usuario es mayor de edad, muestre todos sus datos
#si el usuario NO es mayor de edad, muestre un mensaje indicando que es menor de edad

nombre = input('ingrese su nombre: ')
str_edad = input('ingrese su edad: ')
edad = int(str_edad)
titulo = input('ingrese su titulo: ')
if edad >= 18:
    print (f'usted es mayor de edad, su nombre es {nombre}, su edad es {edad} y su titulo es {titulo}')
else:
    print ('usted es menor de edad')