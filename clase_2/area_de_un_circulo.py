pi = 3.1415


r = float (input('Ingresa el valor del radio en m: '))

if r<0:
    print ('No seas ganzo, es negativo :)')
else:
    if r==0:
        print ('Es un punto jaja')
    else:
        print ('El área es ', r*pi, 'm2')