n = int(input())
for j in range(n):
    print(" " * (n - 1) + "1" + " " * (n - 1), end=" ")
print()
for i in range(1, n - 1):
    for j in range(n):
        print(
            " " * (n - i - 1)
            + str(i + 1)
            + " " * (i * 2 - 1)
            + str(i + 1)
            + " " * (n - i - 1),
            end=" ",
        )
    print()
for j in range(n):
    print(str(n) * (2 * n - 1), end=" ")
