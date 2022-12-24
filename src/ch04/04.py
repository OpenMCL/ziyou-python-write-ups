import random

n = int(input())
ans = [random.randint(1, 9) for j in range(3)]
for i in range(n):
    for j in ans:
        print((str(j) + " ") * n, end=" ")
    print()
