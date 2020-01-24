dic = { 'Diego':['Vásquez', '965246084', 'diego.vasquez.l@uni.pe'],
        'Lucas':['Valverde', '123311323', 'valverdesa@uni.pe']}


def menu ():

    print (#'Hola estimado usuario\n\n',

    '\n 1. Ver lista de contactos',
    '\n 2. Buscar contacto',
    '\n 3. Agregar un contacto',
    '\n 4. Eliminar un contacto',
    '\n 5. Salir\n')

    n = input ('Escoja una de las opciones: ')
    
    while True:
    
        if n==1:
            mostrar_contacto ()
            
        elif n==2:
            buscar_contacto ()

        elif n==3:
            agregar_contacto ()

        elif n==4:
            eliminar_contacto ()
        
        elif n==5:
            break

        else:
            n = input ('Ingrese un valor correcto: ')


def mostrar_contacto ():

    for post, key in enumerate(dic):
        print (post + 1, key, dic[key])
    print ()


def buscar_contacto (nombre):

    if nombre in dic:
        print (nombre, dic[nombre])

    else:
        print ('No existe el contacto')


def agregar_contacto (nombre):

    apellido = input ('Ingrese el apellido: ')
    celular = input ('INgrese el número de celular: ')
    correo = input ('Ingrese el correo')

    dic [nombre] = [apellido, celular, correo]
    mostrar_contactos ()


def eliminar_contacto (nombre):

    dic.pop(nombre)
    mostrar_contactos ()


menu ()
