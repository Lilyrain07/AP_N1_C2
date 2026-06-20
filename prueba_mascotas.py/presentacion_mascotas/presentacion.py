from data.datos_mascotas import listado_mascotas, mascota_encontrada,buscar_mascota
from prettytable import PrettyTable
from presentacion_mascotas.presentacion import menu_principal, titulo_principal

def menu_principal():
    while True:
        print()
        print(titulo_principal)
        print('=' * len(titulo_principal))
        for clave, valor in menu_principal():
            print(f'[{clave}] {valor}')
        opcion_usuario = input('Seleccione una opción: ')

        if opcion_usuario == '1':
            buscar_mascota()
            nombre_mascota = input('Ingrese el nombre de la mascota a buscar: ')
            if mascota_encontrada:
                tabla = PrettyTable()
                tabla.field_names = ['Nombre', 'Raza', 'Edad']
                tabla.add_row([mascota_encontrada['nombre'], mascota_encontrada['raza'], mascota_encontrada['edad']])
                print(tabla)
            else:
                print(f'No se encontró una mascota con el nombre "{nombre_mascota}".')  

        elif opcion_usuario == '2':
            print('¡Hasta luego!')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción del menú.')