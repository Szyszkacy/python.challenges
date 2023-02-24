user_input = input('write something ')

if len(user_input) < 5:
    print('input is less than 5 characters')
elif len(user_input) == 5:
    print('input is  5 characters long')
else:
    print('it is more than 5 characters') 
