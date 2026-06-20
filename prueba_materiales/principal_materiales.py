from datos_prueba.datos_materiales import obtener_inventario_completo
from presentacion_materiales.presentacion import desplegar_interfaz

if __name__ == "__main__":
    datos_materiales = obtener_inventario_completo()
    desplegar_interfaz(datos_materiales)