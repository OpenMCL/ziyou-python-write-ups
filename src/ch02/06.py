n = int(input())

print("*" + " " * (2 * (n - 1) - 1) + "*" + " " * (2 * (n - 1) - 1) + "*")
for i in range(n - 2):
    print(
        " " * (i + 1)
        + "*"
        + " " * (2 * (n - 2 - i) - 1)
        + "*"
        + " " * (2 * (i + 1) - 1)
        + "*"
        + " " * (2 * (n - 2 - i) - 1)
        + "*"
    )

print(" " * (n - 1) + "*" + " " * (2 * (n - 1) - 1) + "*")
