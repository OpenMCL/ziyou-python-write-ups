import random

n = input()
num = [
    (15, 9, 9, 9, 15),
    (2, 2, 2, 2, 2),
    (15, 1, 15, 8, 15),
    (15, 1, 15, 1, 15),
    (9, 9, 15, 1, 1),
    (15, 8, 15, 1, 15),
    (15, 8, 15, 9, 15),
    (15, 1, 2, 2, 2),
    (15, 9, 15, 9, 15),
    (15, 9, 15, 1, 15),
]
nos = [int(s) for s in list(n)]
ran = [random.randint(0, 4) for i in range(len(nos))]
for i in range(9):
    print("-", end="")
    for j in range(len(nos)):
        m = nos[j]
        for k in range(3, -1, -1):
            if i >= ran[j] and i - ran[j] <= 4 and (num[m][i - ran[j]] >> k) % 2:
                print(m, end="")
            else:
                print("-", end="")
        print("-", end="")
    print()
