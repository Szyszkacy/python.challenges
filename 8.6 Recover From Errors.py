#ex1
while True:
    try:
        user_input = int(input('type number '))
        print(user_input)
        break
    except ValueError:
        print('Try again')

#ex2

try:
    str_input = input('Type something ')
    int_input = int(input('Type some number '))
    print(str_input[int_input])
except ValueError:
    print('Type some number must be number')
except IndexError:
    print('Number is too high')

