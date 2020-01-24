variable = 1923


def saludo (nombre, edad):
    #global variable
    #variable += 123
    print (f'Hello {nombre}, are you {edad}')
    print (variable)

def despedida ():
    print ('Bye')
    print (variable)

saludo ('Diego', 17)
despedida ()
#saludo ('Perro', 12)
#saludo ('Gato',11)
#saludo ('You', 100)
#saludo ('Me', 21)
#saludo ('world', 10)


#x = 2/3
#print (f'{x:.2f}')