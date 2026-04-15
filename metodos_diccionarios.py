#defnimos u  nuevo diccionario

datos_personales = {
    'nombre': 'Elisa Arias', 
    'edad' : 18, 
    'titulo' : 'analista programadora'
}

print (datos_personales)

#el metodo KEYS permite ontener las CLAVES del diccionario dict_keys
claves = datos_personales.keys()
print(claves)

#el metodo GET permite obtener valores de datos por su clave
nombre = datos_personales.get('nombre')
print (nombre)

#agregamos elementos al diccionario definiendo una nueva clave con un nuevo valor

rut= input('ingrese su rut: ')
datos_personales['rut'] = rut
print(datos_personales)

#eliminamos un elemento del diccionario con el metodo POP
#el metodo pop elimina el elemento indicado por la clave 

datos_personales.pop('rut')
print(datos_personales)

#el metodo CLEAR elimina todos los elementos del diccionario, dejando un diccionario vacio
datos_personales.clear()
print(datos_personales)
