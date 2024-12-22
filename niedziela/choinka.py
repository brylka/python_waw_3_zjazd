import random

p = 10

for a in range(p):
    for b in range(a):
        if random.randint(0, 10) == 0:
            print('O', end="")
        else:
            print('*', end="")
    print()
