#Metodos para trabajar con listas

animales = ['gato', 'perro', 'conejo', 'vaca', 'Ornitorrinco', 'murcielago']
frutas = ['durazno', 'fresa', ' mango', 'melon']

print(animales)
nuevo_animal = input("Ingrese un nuevo animal: ")
animales.append(nuevo_animal)
print(animales)
#APPEND agrega un nuevo elemento al final de la lista


print(len(animales))
#el metodo INSERT permite agregar un nuevo elemento en la posicion que se indique como argumento

otro_nuevo_animal = input("Ingrese otro nuevo animal: ")
animales.insert(0, otro_nuevo_animal)
print(animales)

# el metodo EXTEND permite agregar varios elementos a una lista
animales.extend(['oveja', 'cerdo'])

print(animales)
animales.extend(frutas)
print(animales)