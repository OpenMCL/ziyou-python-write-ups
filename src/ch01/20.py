n = int(input("> "))
for i in range(n):
    for k in range(i + 1):
        print(str(((i * (i + 1)) // 2 + 1 + k) % 10) * (2 * n - 1), end=" ")
    print()
    for _ in range(n - 2):
        for k in range(i + 1):
            print(
                str(((i * (i + 1)) // 2 + 1 + k) % 10)
                + " " * (2 * n - 3)
                + str(((i * (i + 1)) // 2 + 1 + k) % 10),
                end=" ",
            )
        print()
    for k in range(i + 1):
        print(str(((i * (i + 1)) // 2 + 1 + k) % 10) * (2 * n - 1), end=" ")
    print()
    print()
