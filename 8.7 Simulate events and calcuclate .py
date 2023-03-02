from random import randint

def roll():
    return randint(1,6) 

rolls = 10_000
total = 0

for trial in range(rolls):
    total = total + roll()

av_roll = total / rolls

print(f"The average result of {rolls} rolls is {av_roll}")
