n = int(input("> "))

m = int((n) / 2)
for i in range(n + m):
    for j in range(n):
        if j % 2 == 0:
            if i >= n:
                print(" " * n, end=" ")
            else:
                print(str(j + 1) * (i + 1) + " " * (n - i - 1), end=" ")
        else:
            if i < m:
                print(" " * n, end=" ")
            else:
                print(" " * (i - m) + str(j + 1) * (n - i + m), end=" ")
    print()
