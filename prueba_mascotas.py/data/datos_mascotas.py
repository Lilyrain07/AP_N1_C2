listado_mascotas = [{'nombre': 'nala', 'raza': 'perro', 'edad': '3 años'}
                    , {'nombre': 'michi', 'raza': 'gato', 'edad': '2 años'}
                    , {'nombre': 'tortuga', 'raza': 'tortuga', 'edad': '10 años'}
                    , {'nombre': 'perry', 'raza': 'perico', 'edad': '1 año'}]

def mascota_encontrada(nombre):
    for mascota in listado_mascotas:
        if mascota['nombre'].lower() == nombre.lower():
            return mascota
    return None

def buscar_mascota(nombre):
    for mascota in listado_mascotas:
        if mascota['nombre'].lower() == nombre.lower():
            return mascota
    return None