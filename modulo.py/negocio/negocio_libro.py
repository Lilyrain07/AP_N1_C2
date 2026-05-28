from presentacion import solicitar_dato

def procesar_libro():
    titulo_libro = isbn = editorial = paginas = categoria = ''
    titulo_libro = solicitar_dato(titulo_libro,'Título')
    print(titulo_libro.title())