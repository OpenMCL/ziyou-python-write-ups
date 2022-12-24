n = int(input())
for i in range(n):
    for j in range(n):
        print(
            str((2 * j + 1) % 10) * (n - i) + "/" + str((2 * (j + 1)) % 10) * (i + 1),
            end=" ",
        )
    print()
