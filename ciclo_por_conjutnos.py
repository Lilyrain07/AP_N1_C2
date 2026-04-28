conjunto_numeros = {10,20,30,40,50}
lista_numeros = []
for numero in conjunto_numeros:
    print(numero)

print()
for elemento in conjunto_numeros:
    resultado = elemento * 100
    lista_numeros.append(resultado)
    print(resultado)

print()
print(conjunto_numeros)