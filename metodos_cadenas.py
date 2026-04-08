nombre_personal = 'elisa arias'
titulo_personal = 'estudiante'
ciudad = 'TEMUCO'

#El metodo DIR nos indica todos los metodos disponibles para la variable
print(dir(nombre_personal))

print(f" su nombre personal CAPITALIZADO: {nombre_personal.capitalize()}")
print(f'su nombre personal MAYUSCULAS: {nombre_personal.upper()}')
print(f' su nombre personal como TITULO: {nombre_personal.title()}')
print (f'su ciudad en MINUSCULAS: {ciudad.lower()}')

print(titulo_personal.count('e'))
print(titulo_personal.count('x'))

print(titulo_personal.find('elisa'))
print(titulo_personal.index('estudiante'))