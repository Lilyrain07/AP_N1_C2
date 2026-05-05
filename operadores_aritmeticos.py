#operadores aritmeticos
#operador SUM

suma= 25 +45
print(suma)

concatenacion= 'hola' + ' ' + 'queridos estudiantes'
print(concatenacion)

#operador resta
resta = 25-45
print(resta)

#operador multiplicacion
multiplicacion= 25*45
print(multiplicacion)

multiplicacion_2 = 'hola' *5
print(multiplicacion_2)

#operador division 
division=45/25
print(division)

division_0 = 25/0
print(division_0)

def division (a,b):
    try:
        resultado = a/b
        print (resultado)
    except ZeroDivisionError:
        print('no se puede dividir por 0!')    
    except Exception as error:
        print (f'error en la operacion: {error}')

division(25,0)
