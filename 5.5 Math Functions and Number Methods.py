#ex1
user_number = input('enter a number ')
number = float(user_number)
print(f'{user_number} rounded to 2 decimal places is {round(number,2)}')

#ex2
user_number1 = input('enter a number')
number1 = float(user_number1)
print(f'The absoulte value of {user_number1} is {abs(number1)}')

#ex3
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(
    f"The difference between {num1} and {num2} is an integer? "
    f"{(num1 - num2).is_integer()}!")
