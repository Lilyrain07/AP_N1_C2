nombre_personal = 'elisa arias'
titulo_personal = 'analista programadora estudiante de ingenieria en informatica'
ciudad = 'TEMUCO'
rut_personal = '12345678-9'
rut_completo = '123456789'
texto_multiple_lineas = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,' \
' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ' \
'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ' \
'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.' \
' Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

#El metodo DIR nos indica todos los metodos disponibles para la variable
print(dir(nombre_personal))

#metodos de cadena modifican el string asociado
#CAPITALIZE convierte la primera letra de la cadena en mayuscula y el resto en minuscula
#UPPWER convierte todas las letras en mayusculas
#TITLE convierte la primera letra de cada palabra en mayuscula y el resto en minuscula
#LOWER convierte todas las letras en minusculas
#COUNT cuenta el numero de veces que aparece un caracter o una subcadena dentro de la cadena
#COUNT devuelve 0 si no encuentra el caracter 
#FIND busca un substring dentro de la cadena y devuelve la posicion de la primera ocurrencia
#FIND si no encuentra el substring devuelve -1
#INDEX busca un substring dentro de la cadena y devuelve la posicion de la primera ocurrencia
#INDEX si no encuentra el substring devuelve un error porque no existe el substring
#STRING es una cadena de texto de ninguna, una o mas palabras
#SUBSTRING es una cadena DENTRO de otra cadena

#el metodo LEN permite conocer el largo de los elementos 
print(len(nombre_personal))

print(f" su nombre personal CAPITALIZADO: {nombre_personal.capitalize()}")
print(f'su nombre personal MAYUSCULAS: {nombre_personal.upper()}')
print(f' su nombre personal como TITULO: {nombre_personal.title()}')
print (f'su ciudad en MINUSCULAS: {ciudad.lower()}')

print(titulo_personal.count('e'))
print(titulo_personal.count('x'))

print(titulo_personal.find('isa'))
print(titulo_personal.index('diante'))
#print(titulo_personal.index('x')) 

titulo_personal_split = titulo_personal.split(' ')
print(titulo_personal_split)

rut_split = rut_personal.split('-')
print(rut_split)
print(f'rut: {rut_split[0]}')
print(f'digito verificador: {rut_split[1]}')

rut_completo_split = rut_completo.split('-')
print(rut_completo_split[-1])

print(len(texto_multiple_lineas))
