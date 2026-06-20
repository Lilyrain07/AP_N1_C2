def obtener_materiales_bajo_minimo(lista_materiales):
    STOCK_MINIMO = 5
    materiales_criticos = []
    
    for material in lista_materiales:
        if material["cantidad"] < STOCK_MINIMO:
            materiales_criticos.append(material)
            
    return materiales_criticos