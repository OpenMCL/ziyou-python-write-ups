n = int(input())

print(
    "1"
    + " " * (2 * (n - 1) - 1)
    + str((2 * n - 1) % 10)
    + " " * (2 * (n - 1) - 1)
    + str((4 * n - 3) % 10)
)
for i in range(n - 2):
    print(
        " " * (i + 1)
        + str((2 + i) % 10)
        + " " * (2 * (n - 2 - i) - 1)
        + str((2 * n - 2 - i) % 10)
        + " " * (2 * (i + 1) - 1)
        + str((2 * n + i) % 10)
        + " " * (2 * (n - 2 - i) - 1)
        + str((4 * n - 4 - i) % 10)
    )

print(" " * (n - 1) + str(n % 10) + " " * (2 * (n - 1) - 1) + str((3 * n - 2) % 10))
