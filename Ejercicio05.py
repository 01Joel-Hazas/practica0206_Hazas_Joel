# Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas, hasta que el usuario introduzca la palabra “terminar”.
# El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará
# el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

traduccion = {}

terminar = True
while terminar:
    palabras = input("Introduce la traducción de palabras en formato español:ingles: ")
    for i in palabras.split(','):
        clave, valor = i.split(':')
        traduccion[clave] = valor
    terminar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in traduccion:
        print(traduccion[i], end=' ')
    else:
        print(i, end=' ')

