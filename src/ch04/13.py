import random

n = int(input("> "))
r = [i for i in range(-5, 6) if i != 0]
s = [random.choice(r) for _ in range(n)]

for i in range(6, -7, -1):
    for j in s:
        if abs(i) == abs(j) + 1 and i * j > 0:
            print("{:>2}".format(j), end=" ")
        elif abs(i) <= abs(j) and i * j > 0:
            print(" |", end=" ")
        elif i == 0:
            print("==", end="=")
        else:
            print("  ", end=" ")
    print()
