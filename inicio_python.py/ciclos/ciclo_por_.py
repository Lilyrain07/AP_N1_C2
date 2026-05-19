# Ciclo for (por) para iterar LISTAS 
#recorro cada uno de los elementos de la lista

lista_bandas = ['artic monkeys', 'twenty one pilots', 'imagine dragons', 'manesking']
nombre_personal = 'Elisa Arias'
#usamos el metodo range para crear un rango de numeros
#si a range le damos un argumentos, creara una lista de numeros de la cantidad entregada
#la lista comienza en el indice 0
lista_numeros = range(5)

#si a range le damos 2 elementos le indicamos desde donde inicia y lel elemento final -1

lista_numeros_2 = range(1,11)
#si a range le indicamos donde inicia, el elemento final -1 y el avance entre cada elemento, se llama paso 
lista_numeros_3 = range(1,11,2)

banda_encontrada = False
buscar_banda = input ('que banda desea buscar?')

for banda in lista_bandas:
     banda_mayusculas = banda.upper()
     if banda_encontrada ==True:
          print ('banda encontrada')
     else: print ('banda no encontrada')

    

for letra in nombre_personal:
        print(letra)

print ()
for numero in lista_numeros:
    print(numero * 5)

print()
for elemento in lista_numeros_2:
    resultado = elemento * 2
    print(resultado)
print ()
for elemento in lista_numeros_3:
    print(elemento)