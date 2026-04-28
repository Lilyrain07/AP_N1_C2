#Teniendo 3 escala de temperatura(celsius,fahrenheit y kelvin)
#Cree un conversor de temperaturas que le pida al usuario la escala inicial a la que desea convertir
#y el valor inicial de temperratura

#C° a F° = 1,8°C + 32°
#F° a C°= 5/9(F°-32)

#C° a K° = C° + 273
#K° a C° = 1,8°C + 32°

#F° a K° =(5/9(F°-32)) + 273°
#K° a F° = 1,8°C + 32°
print('sistema conversor de temperaturas')

print ('ingrese escala inicial')
print ('c para celcius')
print('k para kelvin')
print ('f para fahrenheit')

escala_inicial = input('ingrese escala inicial: ').upper()
str_temperatura = input('ingrese la temperatura: ')
escala_final =input ('ingrese escala final: ').upper()

if str_temperatura.isdigit():
    temperatura = float(str_temperatura)
else:
    print ('el valor de temperatura NO es valido.')

if escala_inicial == 'F': 
    if escala_final == 'K':
         resultado = (5/9(temperatura - 32)) + 273
    elif escala_final == 'C':
        resultado = 5/9(temperatura-32)
else:
    print ('escala final no valida')


if escala_inicial == 'C': 
    if escala_final == 'K':
         resultado = (temperatura + 273)
    elif escala_final == 'F':
        resultado = 1,8*temperatura + 32
    print ('escala final no valida')

if escala_inicial == 'K': 
    if escala_final == 'F':
         resultado = (1,8*temperatura + 32)
    elif escala_final == 'C':
        resultado = 5/9(temperatura-32)
else:
    print ('escala final no valida')