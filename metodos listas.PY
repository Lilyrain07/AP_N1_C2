#Metodos para trabajar con listas

animales = ['gato', 'perro', 'conejo', 'vaca', 'Ornitorrinco', 'murcielago']
frutas = ['durazno', 'fresa', ' mango', 'melon']
numeros = [5,7,17,22,1755]

print(animales)
nuevo_animal = input("Ingrese un nuevo animal: ")
animales.append(nuevo_animal.title)
print(animales)
#APPEND agrega un nuevo elemento al final de la lista


print(len(animales))
#el metodo INSERT permite agregar un nuevo elemento en la posicion que se indique como argumento

otro_nuevo_animal = input("Ingrese otro nuevo animal: ")
animales.insert(0, otro_nuevo_animal.title())
print(animales)

# el metodo EXTEND permite agregar varios elementos a una lista
animales.extend(['oveja', 'cerdo'])

print(animales)
animales.extend(frutas)
print(animales)
#el metodo POP elimina el ultimo elemento de la lista, pero tambien puede eliminar un elemento en una posicion especifica si se le indica como argumento
#si no se le indica un argumento, el metodo POP elimina el ultimo elemento de la lista
#POP con argumento INDICE elimina el elemento en la posicion indicada por el indice

animales.pop()
print(animales)
animales.pop(3)
print(animales)
#el metodo REMOVE elimina la primera ocurrencia del elemento indicado como argumento
animales.remove('vaca')
print(animales)
#el metodo CLEAR elimina todos los elementos de la lista, dejando una lista vacia
animales.clear()   
print(animales)

#ordenando listas
#si la lista es de strings se ordena alfabeticamente, si la lista es de numeros se ordena de menor a mayor
#si indicamos reverse=True, la lista se ordena de mayor a menor
animales.sort()
print(animales)
numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)
