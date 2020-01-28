triangle = [0]*3


def validate_number(possible_number):
    
    try:
        possible_number = float (possible_number)
    except ValueError:
        return 2
    else:
        return positive_number(possible_number)


def positive_number(number):

    if number > 0:
        return 1

    else:
        return 3


for index in range (0, len(triangle)):
    
    
    while True:

        triangle[index] = input ('Type a number: ')
        validator = validate_number(triangle[index])

        if validator == 1:
            triangle[index] = float (triangle[index])
            break
        elif validator == 2:
            print('The value you\'ve just typed is not an number')
        else:
            print('The number is negative or 0.')

print (triangle)