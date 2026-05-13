# Los ejercicios a resolver deben incluirse dentro de un menú
# mediante el cual se ejecutará cada uno de ellos.

# 1.- Escriba una función que al ser llamada imprima el saludo "Buen día!"
def saludo_cordial():
    saludo = '!Buen día!'
    return saludo

# 2.- Escriba una función que solicite al usuario ingresar su nombre
# en una variable nombre_usuario
# y al ser llamada imprima el saludo "!Buen día 'nombre_usuario'!"
def saludo_personal():
    saludo = saludo_cordial()
    saludo_mod = saludo.split('!')
    saludo_mod_2 = saludo.replace('!',' ')
    nombre_usuario = solicitar_nombre_usuario()
    saludo_1_split = saludo_mod[0] + ' ' + nombre_usuario + '!'
    saludo_2_split = f'{saludo_mod[0]} {nombre_usuario}!'
    saludo_1_replace = saludo_mod_2 + nombre_usuario + '!'
    saludo_2_replace = f'{saludo_mod_2}{nombre_usuario}!'
    return saludo_1_split + '\n' + saludo_2_split + '\n' + saludo_1_replace + '\n' + saludo_2_replace

def solicitar_nombre_usuario():
    nombre_usuario = input('Ingrese su nombre: ')
    return nombre_usuario.title()


# 3.- Escribir una función que pida al usuario un número entero menor a 10
# y al ser llamada entregue el factorial de ese número
def factorial():
    numero = int(input('Ingrese un número entero: '))
    resultado = 1
    for valor in range(1,numero + 1):
        resultado = resultado * valor
    return f'{numero}! = {resultado}'
#4.- solicite al usuario que ingrese 3 noras y calcular el promedio indicando si el alumno aprueba 
#(nota >= 4.0) o reprueba (nota< 4.0)

def promedio():
    nombre_estudiante =solicitar_nombre_usuario()
    notas_estudiante = []
    cantidad_notas = 3

while len(notas_estudiante) <= cantidad_notas:
    nota = ingreso_notas()
    if nota:
        notas_estudiante.append(nota)


       
def ingreso_notas():
    nota_minima = 1.0
    nota_maxima = 7.0
    try:
        nota = float(input('Ingrese una nota: '))
        if nota >nota_minima and nota <= nota_maxima:
            return nota
        else:
            print(f'nota debe estar entre {nota_minima} y {nota_maxima}')
    except ValueError:
        print('valor ingresado invalido.')
        return ingreso_notas()
    except Exception as error:
        print(f'Error inesperado: {error}')
        return ingreso_notas()



def menu_principal():
    diccionario_menu = {
        '1': 'saludo_cordial',
        '2': 'saludo_personal',
        '3': 'factorial',
        '4': 'promedio',
        '0': 'Salir'
    }
    titulo = 'ejercicios evaluacion 2'
    print(titulo)
    print(f'{'=' * len(titulo)}')
    
    for clave ,valor in diccionario_menu.items():
        print ("[' + clave + '] " + valor)

