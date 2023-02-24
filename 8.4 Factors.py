int_input = int(input('Enter a positive integer '))

for div in range(1, int_input +1):
    if int_input % div == 0:
        print(f'{div} is a factor of {int_input}')
