def guardar_libro(titulo,isbn,editorial,paginas,categoria):
    nuevo_libro = {

        'titulo_libro': titulo,
        'isbn': isbn,
        'editorial': editorial,
        'paginas': paginas,
        'categoria': categoria
    }
    listado_libros.append[nuevo_libro]
    for libro in listado_libros:
        print(libro)