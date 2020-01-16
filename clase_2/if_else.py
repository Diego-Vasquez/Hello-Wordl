# x= 10

# #print('Pedro tiene', x, 'años.')
# #print('Pedro tiene {x} años.'.format(x))
# #print(f'Pedro tiene {x} años.')

# print (type (x))


# #Operadores Aritméticos
# #x = 20 
# print (x)
# x += 31 # x = x + 31
# print (x)
# x -= 1 # x = x -1
# print (x)
# x *= 2 # x = x*2
# print (x)
# x /= 4 # x = x/4
# print (x)

# print (type (x))

# x = x**4
# print (x)

# x = x//279
# print (x) 

# x = x % 9
# print (x)

name = input ('What\'s is your name?')
age = int (input('How old are you?'))

if age < 0:
    print ('Error! An age can\'t be negative')
else:
    print ('Hi',name, '\b!')
    print ('You are', age , 'years old')
    
    if age > 18:
        print ('You are allowed to enter')
    else:
        print ('You shall not pass')
