from data.datos_mascotas import listado_mascotas

def buscar_mascota(nombre):
    nombre = nombre.capitalize()
    for mascota in listado_mascotas:
        if mascota['nombre'] == nombre:
            return mascota
    return None