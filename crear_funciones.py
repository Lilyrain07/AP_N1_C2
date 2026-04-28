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


'''

print (' BIENVENIDO A MI PRIMERA CALCULADORA')
print('===========================')
ciclo = True

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
        suma(a,b)
    elif opcion == '2':
        resta(a,b)
    elif opcion =='3':
        multiplicacion(a,b)
    elif opcion == '4':
        division(a,b)
    else:
     print('opcion no valida')