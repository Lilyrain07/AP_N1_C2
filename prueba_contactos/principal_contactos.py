from datos_contactos import obtener_contactos
from presentacion_contactos import desplegar_interfaz_contactos

if __name__ == "__main__":
    datos_crudos = obtener_contactos_registrados()
    desplegar_interfaz_contactos(datos_crudos)