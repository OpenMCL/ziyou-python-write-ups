n = int(input())
for i in range(n):
    print(" " * (n + 1) * i, end="")
    for j in range(n - i):
        print(str(j + 1 + i) * n, end=" ")
    print()
