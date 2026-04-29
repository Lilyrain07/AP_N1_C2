# Dentro del lenguaje, tenemos la opción de crear nuestras PROPIAS funciones
# para eso usamos la palabra reservada DEF
''''
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
'''

def pedir_datos():
    str_num_1= input('ingrese primer numero: ')
    str_num_2= input('ingrese segundo numero: ')

    num_1 = convertir_float(str_num_1)
    num_2 = convertir_float(str_num_2)

    if num_1 and num_2 != False:
        return num_1 and num_2
    else:
        return (False,False) 

    if num_1.isdigit() and num_2.isdigit():

        num_a= float(num_1)
        num_b = float(num_2)
    else:
        print('valor NO corresponde a un numero')
    return(num_a,num_b)

def convertir_float(valor):
    try:
        return float(valor)
    except (ValueError, TypeError):
        return False


print(' BIENVENIDO A MI PRIMERA CALCULADORA')
print('                                   ')
ciclo = True

def resta(a,b):
    resultado= a-b
    print (f'{a}-{b}= {resultado}')

def suma (a,b):
    resultado = a+b
    print (f'{a}+ {b} = {resultado}')

def multiplicacion(a,b):
    resultado = a*b
    print (f'{a}*{b} = {resultado}')

def division(a,b):
    if b != 0:
        resultado = a/b
        print (f'{a}/{b} = {resultado}')
    else:
        print('DIVISOR INGRESADO:0! no se puede dividir por ese numero')


while ciclo == True:
    print('[1] suma')
    print('[2] resta')
    print('[3] multiplicacion')
    print('[4] division')
    print('[0] salir') 
    opcion= input( 'seleccione su operacion [0-4]: ')

    if opcion == '0':
        ciclo= False
        print ('gracias por usar esta calculadora')
        print ('saliendo...')
    else:
        a,b = pedir_datos()

        if opcion == '1':
            suma (a,b)

        elif opcion == '2':
            resta(a,b)
            
        elif opcion =='3':
            multiplicacion(a,b)
            
        elif opcion == '4':
            division(a,b)
    
        else:
            print('opcion no valida')

        #def es sacronimom de definir porque estamos definiendo una funcion
        #luego de def ponemos el nombre de la funcion
        #luego del nombre, ponemos sus argumentos