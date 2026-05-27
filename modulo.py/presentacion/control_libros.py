from datos import listado_libros
from prettytable import PrettyTable
from datos.data_libros import guardar_libro


def agregar_libro():
    titulo = 'Agregar Libro'
    print(titulo)
    print('=' * len(titulo))
    listar_libros()

    print('\nIngrese los datos del libro:')
    titulo_libro,isbn,editorial,paginas,categoria = solicitar_datos_libro()
    guardar_libro (titulo_libro + isbn + editorial + paginas + categoria)

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
    titulo_libro=isbn=editorial=paginas=categoria = ''

  