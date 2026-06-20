from negocio import buscar_mascota_por_nombre

def mostrar_detalle_mascota(mascota):
    print("-" * 40)
    print("Mascota encontrada con exito:")
    print("Nombre:", mascota["nombre"])
    print("Raza:", mascota["raza"])
    print("Edad:", mascota["edad"], "anos")
    print("-" * 40)

def mostrar_menu():
    while True:
        print("\n==============================")
        print("      MENU DE MASCOTAS        ")
        print("==============================")
        print("1. Buscar mascota")
        print("2. Salir del buscador")
        print("------------------------------")
        
        opcion = input("Selecciona una opcion (1-2): ").strip()
        
        if opcion == "1":
            busqueda = input("\nIntroduce el nombre de la mascota a buscar: ")
            resultado = buscar_mascota_por_nombre(busqueda)
            
            if resultado:
                mostrar_detalle_mascota(resultado)
            else:
                print("-" * 40)
                print("No se encontro ninguna mascota llamada:", busqueda)
                print("-" * 40)
            
        elif opcion == "2":
            print("\nGracias por usar el buscador. Hasta luego.")
            break
        else:
            print("\nOpcion no valida. Por favor, marca 1 o 2.")