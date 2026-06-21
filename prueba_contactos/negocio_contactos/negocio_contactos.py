def generar_lista_nombres_ordenada(lista_contactos):

    contactos_ordenados = sorted(lista_contactos, key=lambda x: x["nombre"])
    return contactos_ordenados