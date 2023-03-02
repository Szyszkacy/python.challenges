import random

def flip_coin():
    if random.randint(0,1)== 0:
        return 'heads'
    else:
        return 'tails'


flips = 0
trials = 10_000

for trial in range(trials):
    if flip_coin() == 'heads':
        flips = flips + 1
    while flip_coin() == 'heads':
        flips = flips + 1
    else:
        flips = flips + 1
        while flip_coin() == 'tails':
            flips = flips + 1
        flips = flips + 1

average_flips = flips / trials

print(f'Average number of flips is {average_flips}')
