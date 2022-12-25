import random

n = int(input("> "))
k = [None for i in range(4)]
for i in range(len(k)):
    k[i] = random.randint(1, 9)
for i in range(2):
    for _ in range(n):
        for j in range(2):
            print((str(k[i * 2 + j]) + " ") * n, end="")
        print()
