from datos import listado_libros
from prettytable import PrettyTable
from negocio import procesar_libro,crear_tabla_libros

def agregar_libro():
    titulo = '\nAgregar Libro'
    print(titulo)
    print('=' * len(titulo))
    listar_libros()

    print('\nIngrese los datos del libro:')
    procesar_libro()


def listar_libros():
    tabla_libros = PrettyTable()

    titulo = '\nListado de Libros'
    print(titulo)
    print('=' * len(titulo))
    tabla_libros = crear_tabla_libros()
    print(tabla_libros)

def modificar_libro():
    titulo = '\nModificar Libro'
    print(titulo)
    print('=' * len(titulo))
    titulo_libro = solicitar_dato(titulo_libro, 'ingrese el titulo del libro')

def eliminar_libro():
    titulo = '\nEliminar Libro'
    print(titulo)
    print('=' * len(titulo))

def solicitar_datos_libro():
    titulo_libro = isbn = editorial = paginas = categoria = ''
    while titulo_libro == '':
        titulo_libro = input('Título: ').strip()
    while isbn == '':
        isbn = input('ISBN: ').strip()
    while editorial == '':
        editorial = input('Editorial: ').strip()
    while paginas == '':
        paginas = input('Cantidad de Páginas: ').strip()
    while categoria == '':
        categoria = input('Categoría: ').strip()
    return titulo_libro,isbn,editorial,paginas,categoria

def solicitar_dato(tipo_dato,mensaje_input):
    while tipo_dato == '':
        tipo_dato = input(f'{mensaje_input}: ').strip()
        return tipo_dato