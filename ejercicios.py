# 1._ escriba unafuncion que calcule el total de una factura tras aplicarle el IVA.
#    la funcion debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
# si la funcion no recibe el porcentaje del IVA, debera aplicar por defecto el 19% 

# 2._ Escriba una funcion que calcule el area de un circulo y otra que calcule 
# el volumen de un cilindro usando la primera funcion del area
import math
import calculadora
from calculadora import convertir_float

def area_circunferencia(radio):
    pi = math.pi
    resultado = pi * radio *radio
    return resultado

def volumen_cilindro(radio, altura):
    area = area_circunferencia(radio)
    resultado = area *altura
    return resultado

def calculo_volumen_cilindro():
    print('ingrese los datos solicitados')
    str_radio= input('radio de cilindro: ')
    str_altura = input ('altura de cilindro: ')
    radio = calculadora.convertir_float(str_radio)
    altura = calculadora.convertir_float(str_altura)
    volumen = volumen_cilindro(radio, altura)
    print(volumen)

#3._ escriba una funcion que permita escribir la tabla de multiplicar de un numero ingresado por el usuario

# tablas de multiplicar

while True:
    print('[1] calculo de IVA')
    print('[2] calculo de volumen cilindro')
    print('[3] tabla de multiplicar')
    print('[0] salir')

    opcion =input ('ingrese su opcion [0-3]')
    valores_opcion = range (4)

    if opcion in valores_opcion:
        if opcion =='1':
            pass
        elif opcion =='2':
            pass
        elif opcion =='3':
            pass
        elif opcion == '0':
            print ('saliendo del sistemaa')
            break
    else:
        print('opcion seleccionada no valida')