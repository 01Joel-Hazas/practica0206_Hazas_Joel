# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

diccionarioMonedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduce una divisa:")

if divisa.title() in diccionarioMonedas:
    print(diccionarioMonedas[divisa.title()])
else:
    print("No se encuentra la divisa introducida.")