from data.datos_mascotas import obtener_lista_mascotas

def buscar_mascota_por_nombre(nombre_buscado):
    nombre_limpio = nombre_buscado.strip().lower()
    lista_mascotas = obtener_lista_mascotas()
    
    for mascota in lista_mascotas:
        if mascota["nombre"].lower() == nombre_limpio:
            return mascota
            
    return None