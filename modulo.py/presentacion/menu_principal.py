from datos import datos_menu
from datos import numero_version

titulo = 'Sistema Gestión Biblioteca'

def menu_principal():
    print(f'\n{titulo} v{numero_version}')
    print(f'{'=' * len(titulo)}=={'=' * len(numero_version)}\n')
    
    for clave, valor in datos_menu.items():
        print(f'[{clave}]. {valor}')
opcion_usuario = seleccionar_opcion()
print(opcion_usuario)

def seleccionar_opcion():
    opcion = input(f'seleccione su opcion: [0-{len(datos_menu) - 1}] ')
    return opcion

