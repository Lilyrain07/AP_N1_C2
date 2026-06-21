from negocio_contactos.negocio_contactos import generar_lista_nombres_ordenada

def mostrar_contactos_completos(lista_contactos):
    print("========================================")
    print("   LISTADO DE CONTACTOS ALFABETICO")
    print("========================================")
    
    if not lista_contactos:
        print("No hay contactos registrados en la agenda.")
    else:
        for posicion, contacto in enumerate(lista_contactos, 1):
            
            print(f"{posicion}. Nombre: {contacto['nombre']}  Numero: {contacto['numero']}")
            
    print("----------------------------------------")

def desplegar_interfaz_contactos(lista_contactos):
    print("Iniciando agenda de contactos...")
    contactos_procesados = generar_lista_nombres_ordenada(lista_contactos)
    mostrar_contactos_completos(contactos_procesados)