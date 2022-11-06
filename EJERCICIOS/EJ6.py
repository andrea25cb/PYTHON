#1.Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#2.Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#3.Preguntar por el NIF del cliente y mostrar sus datos.
#4.Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#5.Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#6.Terminar el programa.
#creo un diccionario con los datos:

clientes = {}
opcion = ''
while opcion != '6':
    if opcion == '1':#añadir cliente nuevo
        nif = input('Introduce NIF del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        telefono = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        preferente = input('¿Es un cliente preferente (y/n)? ')
        #añado los datos al otro diccionario: clientes se vería así?:
        #el numero es la clave, los datos el valor
        #dict [clave] = valor == clientes[nif] = datos

        datos = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':preferente=='y'}
        #por lo que cada vez que pongo un nif, llamo al array de datos de cada cliente:
        #insertamos diccionario cliente en dict clientes
        clientes[nif] = datos
    if opcion == '2':#borrar cliente
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes: 
            del clientes[nif]
            print("CLIENTE ELIMINADO")
        else:
            print('No existe cliente con el nif', nif)
    if opcion == '3':#mostrar cliente
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('____________________________')
            print("DATOS DEL CLIENTE:")
            print('----------------------------')
            print('NIF: ',nif)
            for clave, valor in clientes[nif].items():
                print(clave + ":", valor)
        else:
            print('No existe cliente con el nif', nif)
    if opcion == '4':#LISTAR CLIENTES
        print('____________________________')
        print('LISTA DE CLIENTES:')
        print('----------------------------')
        for clave, datos in clientes.items(): #sale el nif y el nombre, cliente es cliente items devuelve las claves(nif)
            print(clave,datos['nombre']) 
    if opcion == '5':#MOSTRAR CLIENTES PREFERENTES
        print('Lista de clientes preferentes')
        for clave, datos in clientes.items():
            if datos['preferente']:
                print(clave, datos['nombre'])
                
    opcion = input('Menú de opciones\n1. Añadir cliente\n2. Eliminar cliente\n3. Mostrar cliente\n4. Listar clientes\n5. Listar clientes preferentes\n6. Terminar\nElige una opción:')
    