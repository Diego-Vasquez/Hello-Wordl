#Implementar un algoritmo que calcule el area de un triangulo

while a <= 0
    while True:
        try:
            a = float(input('Ingrese la longitud del primer lado del triangulo: '))
        except ValueError:
            print ('Ingrese la longitud en numerales')
        else:
            break
    if a <= 0:
        print (Ingrese un número positivo)
    


b = float(input('Ingrese la longitud del segundo lado del triangulo: '))
c = float(input('Ingrese la longitud del tercer lado del triangulo: '))