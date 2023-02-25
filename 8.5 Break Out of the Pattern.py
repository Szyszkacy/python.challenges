#ex1
while True:
    user_input = input('write q or Q to quit: ')
    if user_input == 'q' or user_input == 'Q':
        break

#ex2

for i in range(1,51):
    if i % 3 == 0:
        continue
    print(i)
