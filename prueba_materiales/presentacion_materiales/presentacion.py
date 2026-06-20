from negocio_prueba.negocio_materiales import obtener_materiales_bajo_minimo

def mostrar_reporte_stock(materiales_criticos):
    print("========================================")
    print("   ALERTA: REPORTE DE STOCK CRITICO")
    print("========================================")
    print("Los siguientes materiales estan por debajo del minimo (5 unidades):")
    print("========================================")
    
    if not materiales_criticos:
        print("Todo el inventario esta en niveles correctos.")
    else:
        for material in materiales_criticos:
            print(f"Material: {material['articulo']}")
            print(f"Cantidad actual: {material['cantidad']} unidades")
            print("========================================")

def desplegar_interfaz(lista_materiales):
    print("Iniciando sistema de control de inventario...")
    materiales_en_alerta = obtener_materiales_bajo_minimo(lista_materiales)
    mostrar_reporte_stock(materiales_en_alerta)