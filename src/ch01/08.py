n = int(input())
for i in range(n):
    print(
        (str(i + 1) + " ") * (i + 1)
        + "  " * (n - i - 1) * 2
        + (str(i + 1) + " ") * (i + 1)
    )
