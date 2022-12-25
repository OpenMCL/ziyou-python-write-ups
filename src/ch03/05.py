n = int(input())
for i in range(n - 1, -1, -1):
    for _ in range(3):
        for j in range(n - 1, -1, -1):
            s = abs(j)
            if n - abs(i) > s:
                print(" " * 3 * i, end="")
                for _ in range(n - j - i):
                    print(str(n - i - j) * 5, end=" ")
                print(" " * 3 * i, end="")
            else:
                print(" " * 6 * (n - j), end="")
        print()
