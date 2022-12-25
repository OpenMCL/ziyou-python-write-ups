n = int(input("> "))
for i in range(n - 1):
    print(
        " " * (2 * (i))
        + str((2 * i + 1) % 10)
        + "-" * ((n - i - 1) * 4 - 1)
        + str((2 * (i + 1)) % 10)
        + " " * 2 * i
    )
print(" " * 2 * (n - 1) + str((2 * n - 1) % 10) + " " * 2 * (n - 1))
