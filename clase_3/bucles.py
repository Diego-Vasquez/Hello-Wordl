

#num = int (input('Ingrese un número: '))

#factorial = 1
#i=1

#if num < 0:
#    print ('Tiene que ser positivo o cero')
#else:
#    while i <= num:
#        factorial *= i
#        i +=1
#    print (f'El factorial es {factorial}')
#
#    answer = ''
#
#    while answer 
#
#    for var in range (7):
#       print (var), end=' ')


lista = [1, 2, 3.0, True, 'Anthony', False, [1,0,1.9]] 

print (lista)
#print (type(lista))
#print (len(lista)

lista2 = lista[3:6]
lista3 = lista [-1:-5:-1]
print (lista2)
print (lista3)

print()

lista.append ('hola')
print (lista)
print ()

lista.pop (3)
print (lista)
print ()

conjunto = set ()
conjunto = {1, 2 ,3, 1, 2, 3, 4, 5, 4, 5}
conjunto2 = {1, 2 ,3, 1, 2, 3, 4, 5, 4, 5, 9, 8}

print (conjunto)

conjunto.add(6)

print (conjunto)
print ()

conjunto.discard (1)
print (conjunto)
print (conjunto2)
print ()

c = conjunto | conjunto2  #Union
print (c)
print ()

c = conjunto & conjunto2
print (c)
print ()

c = conjunto ^ conjunto2
print (c)
print ()

#Diccionarios

dic = {'Diego':'Vaquez', 'perro': 'gato'}
print (dic)

keys = list(dic.keys())
values =list(dic.values())

print (keys)
print (values

#for var in dic:
#    print (var, end='')
#    print ()

for x, key in enumerate(dic):
    print (x + 1, key)

dic ['perro'] = 'Bazán'
print(dic)