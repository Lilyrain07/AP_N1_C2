#ciclo FOR (por) para iterar DICCIONARIOS
#recorro cada uno de los elementos del diccionario

datos_personales ={
    'nombre' : 'armando casas',
    'edad' : 18,
    'profesion' : 'analista'
}

for clave in datos_personales:
    print(clave)

for elemento in datos_personales.items():
    print(elemento)

for elemento in datos_personales.items():
    clave = elemento[0]
    valor = elemento[1]
    print(f'clave: {clave} valor: {valor}')
