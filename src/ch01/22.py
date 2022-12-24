n = int(input())
print("1" + "-" * ((n - 1) * 4 - 1) + "2" + "-" * ((n - 1) * 4 - 1) + "3")
for i in range(1, n - 1):
    for j in range(2):
        print(
            " " * (2 * (i))
            + str((4 * (i) + 2 * j) % 10)
            + "-" * ((n - i - 1) * 4 - 1)
            + str((4 * (i) + 2 * j + 1) % 10)
            + " " * (2 * (i - 1) + 1),
            end="",
        )
    print()
for j in range(2):
    print(
        " " * 2 * (n - 1) + str(((n - 1) * 4 + j) % 10) + " " * (2 * (n - 1) - 1),
        end="",
    )
