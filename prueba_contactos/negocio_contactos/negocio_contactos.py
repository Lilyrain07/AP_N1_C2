import datos_contactos

def generar_lista_ordenada(agenda_contacto):
    nombres = []
    for contacto in agenda_contacto:
        nombres.append(contacto["nombre"])
    
    nombres.sort()
    return nombres