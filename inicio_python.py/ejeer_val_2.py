# Los ejercicios a resolver deben incluirse dentro de un menú
# mediante el cual se ejecutará cada uno de ellos.

mensaje_error_valor = 'Valor Ingresado NO corresponde'

# 1.- Escriba una función que al ser llamada imprima el saludo "Buen día!"
def saludo_cordial():
    saludo = 'Buen día!'
    return saludo

def saludo_cordial_2():
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

def saludo_personal_2():
    saludo = saludo_cordial_2()
    saludo_mod = saludo.rstrip('!')
    saludo_mod_2 = saludo[:-1]
    saludo_mod_3 = saludo[:len(saludo)-1]
    nombre_usuario = solicitar_nombre_usuario()

    saludo_1 = saludo_mod + ' ' + nombre_usuario + '!'
    saludo_2 = saludo_mod_2 + ' ' + nombre_usuario + '!'
    saludo_3 = saludo_mod_3 + ' ' + nombre_usuario + '!'
    
    saludo_4 = f'{saludo_mod} {nombre_usuario}!'
    saludo_5 = f'{saludo_mod_2} {nombre_usuario}!'
    saludo_6 = f'{saludo_mod_3} {nombre_usuario}!'
    return saludo_1 + '\n' + saludo_2 + '\n' + saludo_3 + '\n' + saludo_4 + '\n' + saludo_5 + '\n' + saludo_6

def solicitar_nombre_usuario():
    nombre_usuario = input('Ingrese su nombre: ')
    return nombre_usuario.title()


# 3.- Escribir una función que pida al usuario un número entero menor a 10
# y al ser llamada entregue el factorial de ese número
# 5! = 1 * 2 * 3 * 4 * 5 = 120
def factorial():
    numero = int(input('Ingrese un número entero: '))
    resultado = 1
    for valor in range(1,numero + 1):
        resultado = resultado * valor
    return f'{numero}! = {resultado}'

# 4.- Solicite al usuario ingresar:
# Nombre del estudiante y 3 notas, para calcular el promedio 
# indicando si el alumno aprueba (nota >= 4.0) o reprueba (nota < 4.0)
# Salida Final Programa:

# Nombre Estudiante: nombre
# Notas: notas
# Promedio: promedio
# Situación Final: Aprobado/Reprobado

def calculo_promedio():
    nombre_estudiante = solicitar_nombre_usuario()
    notas_estudiante = []
    numero_notas = cantidad_notas()
    
    if numero_notas:
        while len(notas_estudiante) < numero_notas:
            nota = ingreso_nota()
            if nota:
                notas_estudiante.append(nota)
    
    promedio = sum(notas_estudiante) / len(notas_estudiante)
    situacion_final = ''
    if promedio >= 4.0:
        situacion_final = 'Aprobado'
    else:
        situacion_final = 'Reprobdao'

    resultado = f'''
Nombre Estudiante: {nombre_estudiante.title()}
Notas: {notas_estudiante}
Promedio: {round(promedio,1)}
Situación Final: {situacion_final}
'''
    return resultado

def ingreso_nota():
    nota_minima = 1.0
    nota_maxima = 7.0
    try:
        nota = float(input('Ingrese Nota:'))
        if nota > nota_minima and nota <= nota_maxima:
            return nota
        else:
            print('Nota debe estar entre 1.0 y 7.0')
    except ValueError:
        print(mensaje_error_valor)
    except Exception as error:
        print(f'Error: {error}')

def cantidad_notas():
    try:
        numero = int(input('Ingrese cantidad notas:'))
        return numero
    except ValueError:
        print(mensaje_error_valor)
    except Exception as error:
        print(f'Error: {error}')

def menu_principal():
    diccionario_menu = {
        '1':'Saludo Cordial',
        '2':'Saludo Personal',
        '3':'Saludo Personal 2',
        '4':'Factorial',
        '5':'Calculo Promedio',
        '0':'Salir'
    }
    titulo = 'Ejercicios Evaluación 2'
    print(titulo)
    print(f'{'=' * len(titulo)}')
    while True:
        print()
        for clave,valor in diccionario_menu.items():
            print('[' + clave + '] ' + valor)

        opcion = input('\nIngrese su Opción [0-4]: ')
        valores_opcion = ['0','1','2','3','4','5']

        if opcion in valores_opcion:
            if opcion == '1':
                respuesta = saludo_cordial()
            elif opcion == '2':
                respuesta = saludo_personal()
            elif opcion == '3':
                respuesta = saludo_personal_2()
            elif opcion == '4':
                respuesta = factorial()
            elif opcion == '5':
                respuesta = calculo_promedio()
            elif opcion == '0':
                print('Saliendo del sistema...')
                break
            print()
            print(respuesta)
        else:
            print('Opción ingresada NO corresponde...')

menu_principal()