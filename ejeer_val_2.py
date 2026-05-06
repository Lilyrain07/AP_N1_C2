#los ejercicios a resoolver deben incluirse dentro de un menu
#mediante el cual se ejecutara cada uno de ellos

#1.- escriba una funcion que al ser llamada imprima el saludo "buen dia"

#2.-escruba una funcion que solicite al usuario ingresar su nombre
#en unba variable nombre_usuario

#3.- escribir una funcion que pida al usuario un numero entero menor a 10
#y al ser llamada entregue el factorial de ese numero
import math

def menu_principal():
    while True:
        print()
        print('[1] saludo')
        print('[2] nombre')
        print('[3] factorial')
        print('[0] Salir')

        opcion = input('Ingrese su Opción [0-3]: ')
        valores_opcion = ['0','1','2','3']

        if opcion in valores_opcion:
            if opcion == '1':
                saludo = ('¡Buenos dias estudiante inacap!')
                print(saludo)
            elif opcion == '2':
                nombre_usuario = input('¿cual es su nombre?: ')
                print (f'buenos dias {nombre_usuario} ')
            elif opcion == '3':
                numero= input('ingrese el numero que quiere (debe ser un numero MENOR A 10!): ')
                if numero < 10:
                    resultado = math.factorial(numero)
                    print (f'el resultado de su numero en factoriales es: {numero}! = {resultado} ')
                else:
                    print('numero ingresado no corresponde, intentelo de nuevo.')

            elif opcion == '0':
                print('Saliendo del sistema...')
                break
        else:
            print('Opción ingresada NO corresponde...')

menu_principal()