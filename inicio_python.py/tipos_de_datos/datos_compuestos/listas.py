print('\n Trabajando con LISTAS' )
lista =['armando casas, True, 1.58']
print (lista)

print (type(lista))

print(lista[0])
print(lista[1])
print(lista[2])

print (type(lista[0]))
print (type(lista[1]))
print (type(lista[2]))

str_nombre = input( 'ingrese su nombre: ')
lista [0] = str_nombre #cambio valido, acceso por INDICE
print(lista[0])
print(f"{lista}\n")

int_edad = int(input('ingrese su edad: '))
lista [1] = int_edad
print(lista[1])
print(f"{lista}\n")


int_altura = int(input('ingrese su altura: '))
lista [2] = int_altura
print(lista[2])
print(f"{lista}\n")



