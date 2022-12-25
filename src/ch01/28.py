n = int(input())
for _ in range(n):
    print(" " * n * (n - 1) + str(n) * n)
for i in range(n - 2, -1, -1):
    for _ in range(n):
        print(
            " " * n * i
            + str(i + 1) * n
            + " " * n * (2 * (n - i - 1) - 1)
            + str(i + 1) * n
        )
