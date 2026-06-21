from datos_contactos.datos_contactos import contactos_registrados
from presentacion_contactos.presentacion_contactos import desplegar_interfaz_contactos

if __name__ == "__main__":
    datos_crudos = contactos_registrados()
    desplegar_interfaz_contactos(datos_crudos)