# Dentro del lenguaje, tenemos la opción de crear nuestras PROPIAS funciones
# para eso usamos la palabra reservada DEF

def suma(num_1,num_2):
    # Este será el contenido de la función
    resultado = num_1 + num_2
    print(f'{num_1} + {num_2} = {resultado}')

def resta(num_1,num_2):
    resultado = num_1 - num_2
    print(f'{num_1} - {num_2} = {resultado}')

def multiplicacion(num_1,num_2):
    resultado = num_1 * num_2
    print(f'{num_1} * {num_2} = {resultado}')

def division(num_1,num_2):
    if num_2 != 0:
        resultado = num_1/num_2
        print(f'{num_1} / {num_2} = {resultado}')
    else:
         print ('no se puede dividir por 0')


def pedir_datos():
    num_1= input('ingrese primer numero')
    num_2= input('ingrese segundo numero')


    if num_1.isdigit() and num_2.isdigit():

        num_a= float(num_1)
        num_b = float(num_2)
    else:
        print('valor NO corresponde a un numero')
    return(num_a,num_b)

    

#suma(num_1,num_2)
#resta(num_1,num_2)
#multiplicacion(num_1,num_2)
#division(num_1,num_2)
