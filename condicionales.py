
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

#para evaluar varias condiciones, usamos IF con ELIF

#AB (Clase Alta): Hogares con ingresos superiores a (7.000.000) mensuales
#C1 (Clase Media Alta): Hogares con ingresos entre (2.000.000) y (3.500.000) mensuales
#C2 (Clase Media Baja): Hogares con ingresos entre (562.000) y (2.000.000) mensuales
#DE (Clase Baja): Hogares con ingresos entre  (324.000) y (562.000) mensuales
str_sueldo_mensual = input('ingrese su sueldo mensual: $')
sueldo_mensual = float(str_sueldo_mensual)

if sueldo_mensual >= 7000000:
    print ('usted pertenece a la clase AB')
elif sueldo_mensual >= 3500000:
    print ('usted pertenece a la clase C1')
elif sueldo_mensual >= 2000000:
    print ('usted pertenece a la clase C2')
else:
    print ('usted pertenece a la clase DE')