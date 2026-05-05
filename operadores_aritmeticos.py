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
#cuando tenemos errores logicos podemos hacer control de errores, pero ojo
#los controles de errores se hacen ANTES DE LA OPERACION

def division (a,b):
    try:
        resultado = a/b
        print (resultado)
    except ZeroDivisionError:
        print('no se puede dividir por 0!')    
    except Exception as error:
        print (f'error en la operacion: {error}')

division(25,0)

#operador potencia

potencia= 5**7
print(potencia)

#operador RESTO
#permite obtener el resto de una division
resto = 9.5 % 4.5
print (resto)

