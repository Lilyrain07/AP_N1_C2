from datos import listado_libros

def agregar_libro():
    titulo = 'agregar libro'
    print (titulo)
    print ('=' * len(titulo))
    print('Ingrese los datos del libro:')
    titulo_libro, isbn, editorial, paginas, categoria = solicitar_datos_libro()


def listado_libros():
     titulo= 'listado de libros'
print (titulo)
print ('=' * len(titulo))
print(listado_libros)
for libro in listado_libros:
    orint(libro)

def modificar_libro():
    titulo= 'modificar libro'
print (titulo)
print ('=' * len(titulo))

def eliminar_libro():
    titulo= 'eliminar libro'
print (titulo)
print ('=' * len(titulo))

def solicitar_datos_libro():
    titulo_libro = input ('titulo del libro: ')
    isbn = input ('isbn del libro: ')
    editorial = input ('editorial del libro: ')
    paginas = input ('cantidad de paginas del libro: ')
    categoria = input ('categoria del libro: ')
    return titulo_libro,isbn,editorial,paginas,categoria