n = int(input("> "))
for i in range(-2 * n - 2, 0):
    for w in range(2):
        for j in range(-n + 1 if w == 0 else -n + 2, n):
            a, b = abs(i), abs(j)
            s = n - b
            if s * 2 >= a - 2 and s * 2 - 4 < a - 2:
                print(str(s) * 3, end=" ")
            else:
                print(" " * 3, end=" ")
    print()
