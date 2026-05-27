from datos import listado_libros
from prettytable import PrettyTable


def agregar_libro():
    titulo = 'Agregar Libro'
    print(titulo)
    print('=' * len(titulo))
    print('Ingrese los datos del libro:')
    titulo_libro,isbn,editorial,paginas,categoria = solicitar_datos_libro()

def listar_libros():
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['Título', 'ISBN', 'Editorial', 'Páginas', 'Categoría']

    titulo = 'Listado de Libros'
    print(titulo)
    print('=' * len(titulo))
    for libro in listado_libros:
        tabla_libros.add_row([libro['titulo_libro'], libro['isbn'], libro['editorial'], libro['paginas'], libro['categoria']])
    print(tabla_libros)

def modificar_libro():
    titulo = 'Modificar Libro'
    print(titulo)
    print('=' * len(titulo))

def eliminar_libro():
    titulo = 'Eliminar Libro'
    print(titulo)
    print('=' * len(titulo))

def solicitar_datos_libro():
    titulo_libro = input('Título: ')
    isbn = input('ISBN: ')
    editorial = input('Editorial: ')
    paginas = input('Cantidad de Páginas: ')
    categoria = input('Categoría: ')
    return titulo_libro,isbn,editorial,paginas,categoria

