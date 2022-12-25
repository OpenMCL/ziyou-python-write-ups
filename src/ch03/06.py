n = int(input("> "))
for i in range(-n + 1, n):
    for _ in range(3):
        for j in range(-n + 1, n):
            s = abs(j)
            b = abs(i)
            if n - b > s:
                print(" " * 3 * b, end="")
                for _ in range(n - s - b):
                    print(str(n - b - s) * 5, end=" ")
                print(" " * 3 * b, end="")
            else:
                print(" " * 6 * (n - s), end="")
        print()
