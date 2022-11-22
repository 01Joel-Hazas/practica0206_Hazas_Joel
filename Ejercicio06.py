# Escribir un programa que permita gestionar la base de datos de alumnado de un classroom.
# Los alumnos y alumnas se guardarán en una lista que almacena un diccionario para cada alumno/a en el que la clave
# de cada alumno/a será su NIF, y el valor será otro diccionario con los datos del alumno/a
# (nombre, apellidos, teléfono, correo, aprobado), donde aprobado tendrá el valor True si ha aprobado el módulo.
# El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir alumno/a, (2) Eliminar alumno/a, (
# 3) Mostrar alumno/a, (4) Listar  el alumnado, (5) Listar alumnado aprobado, (6) Terminar.
# En función de la opción elegida el programa tendrá que hacer lo siguiente:
# Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
# Preguntar por el NIF del alumno/a y mostrar sus datos.
# Mostrar lista del alumnado de la base de datos con su NIF y nombre.
# Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
# Terminar el programa.

alumnos = {}
opcion = ''
salir = False;

while not salir:
    if opcion == '1':
        nif = input('Introduce NIF del alumno: ')
        nombre = input('Introduce el nombre del alumno: ')
        aprobado = input('¿Has aprobado? (S/N)? ')
        alumno = {'nombre':nombre, 'aprobado':aprobado=='S'}
        alumnos[nif] = alumno
    elif opcion == '2':
        nif = input('Introduce NIF del alumno: ')
        if nif in alumnos:
            del alumnos[nif]
        else:
            print('No se ha podido encontrar el alumno con el nif', nif)
    elif opcion == '3':
        nif = input('Introduce el NIF del alumno: ')
        if nif in alumnos:
            print('NIF:', nif)
            for clave, valor in alumnos[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el alumno con el nif', nif)
    elif opcion == '4':
        print('Lista del alumnado:')
        for clave, valor in alumnos.items():
            print(clave, valor['nombre'])
    elif opcion == '5':
        print('Listado de alumnos aprobados:')
        for clave, valor in alumnos.items():
            if valor['aprobado']:
                print(clave, valor['nombre'])
    elif opcion == '6':
        salir = True
        break;

    print("Menu de opciones\n-----------------")
    opcion = input("(1) Añadir alumno/a\n(2) Eliminar alumno/a\n(3) Mostrar alumno/a\n(4) Listar todos los alumnos\n(5) Listar el alumnado aprobado\n(6) Terminar el programa.")