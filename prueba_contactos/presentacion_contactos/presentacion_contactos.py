from negocio_contactos import generar_lista_ordenada

def mostrar_nombres_alfabetico(lista_nombres):
    print("========================================")
    print("   LISTADO DE CONTACTOS ALFABETICO")
    print("========================================")
    
    if not lista_nombres:
        print("No hay contactos registrados en la agenda.")
    else:
        for posicion, nombre in enumerate(lista_nombres, 1):
            print(f"{posicion}. {nombre}")
            
    print("----------------------------------------")

def desplegar_interfaz_contactos(lista_contactos):
    print("Iniciando agenda de contactos...")
    nombres_ordenados = generar_lista_ordenada(lista_contactos)
    mostrar_nombres_alfabetico(nombres_ordenados)