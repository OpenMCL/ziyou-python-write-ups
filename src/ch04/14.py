import random

n = int(input("> "))
s = [random.randint(1, 9) for _ in range(n)]

for i in range(10, -1, -1):
    print(" " * i, end="")
    for j in s:
        if i == j + 1:
            print("*", end="  ")
        elif i == 0:
            print(j, end="  ")
        elif i <= j:
            print("/", end="  ")
        else:
            print(" ", end="  ")
    print()
