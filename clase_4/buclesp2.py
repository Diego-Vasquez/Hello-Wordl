tupla = (1, 232, True, 'Dieog', 1, 1)

print (tupla.index(1)) #.index indica la ubicacion del impremer elemento a buscar
print (tupla.count (1) ) #.count  Cuenta cuantos veces se encuentra el elemento

print (type(tupla))

tupla = list (tupla)

print (type(tupla))

tupla = tuple(tupla)

print (type(tupla))

A = set ()
A = {1, 3, 2, 54, 2, 3, 45, 6, 8, 10}

print (type(A))

print (A)

A.discard (1) #Elimina dicho elemento

print (A)

A.remove (8) #TAmbien elimina elementos, pero arooja error si no lo encuentra

print (A, '\n\n\n')

B = {3, 45, 108, 93, 23 ,132}

print (A, '\n', B)

C= A|B #Union
print (C)
C= A&B #Interseccion
print (C)

C= A^B #Dif simetrica
print (C)

C= A-B
print (C, '\n')

#print (A.intersection(B))  # A se intesecta con B
print (A.isdisjoint(B))  # A es disjunto
print (A.issubset(B))   # A es subconjunto de B
print (A.issuperset (B), ' ')   #A contiene a B


dic = { 'Diego':'Vásquez', 'Perro':'Gato'}
print (dic)

keys = list (dic.keys())
values = list (dic.values())

print (keys)
print (values, '\n\n\n')


for post, key in enumerate (dic):
    print (post + 1, key)