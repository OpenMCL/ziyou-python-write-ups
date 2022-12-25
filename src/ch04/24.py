n = input("> ")
nos = [int(s) for s in list(n)]
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
for i in range(5):
    for _ in range(2):
        for k in nos:

            for j in range(3, -1, -1):
                if (num[k][i] >> j) % 2:
                    print(str(k) * 2, end="")
                else:
                    print("  ", end="")
            print(" ", end=" ")
        print()
