from data.datos_mascotas import listado_mascotas, mascota_encontrada
from prettytable import PrettyTable
from presentacion_mascotas.presentacion import menu_principal, titulo_principal


while True:
    titulo = 'Menú Principal'
    print()
    print(titulo)
    print('=' * len(titulo))
    for clave, valor in menu_principal():
        print(f'[{clave}] {valor}')
    opcion_usuario = input('Seleccione una opción: ')

    if opcion_usuario == '1':
        input_nombre = input('Ingrese el nombre de la mascota a buscar: ')
      
        if input_nombre == 'nombre' in listado_mascotas:
            mascota = mascota_encontrada(input_nombre)
            if mascota:
                tabla = PrettyTable()
                tabla.field_names = ['Nombre', 'Raza', 'Edad']
                tabla.add_row([mascota['nombre'], mascota['raza'], mascota['edad']])
                print(tabla)
            else:
                print(f'No se encontró una mascota con el nombre "{input_nombre}".')

    elif opcion_usuario == '2':
        print('¡Hasta luego!')
        break
    else:
        print('Opción no válida. Por favor, seleccione una opción del menú.')

    
def buscar_mascota(nombre):
    for mascota in listado_mascotas:
        if mascota['nombre'].lower() == nombre.lower():
            return mascota
    return None

def mascota_encontrada(nombre):
    for mascota in listado_mascotas:
        if mascota['nombre'].lower() == nombre.lower():
            return mascota
    return 