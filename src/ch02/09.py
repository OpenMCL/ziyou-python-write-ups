n = int(input("> "))
for i in range(n):
    for j in range(1, i + 1):
        print(str(j) + " ", end="")
    print((str(i + 1) + " ") * (2 * (n - i) - 1), end="")
    for j in range(i, 0, -1):
        print(str(j) + " ", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(1, i):
        print(str(j) + " ", end="")
    print((str(i) + " ") * (2 * (n - i) + 1), end="")
    for j in range(i - 1, 0, -1):
        print(str(j) + " ", end="")
    print()
