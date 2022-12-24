n = int(input())
for i in range(-n + 1, n):
    for j in range(-2 * (n - 1), n):
        if (
            i - j == n - 1
            or i + j == -n + 1
            or abs(j - i) == n - 1
            or abs(i) == j
            or j + i == n - 1
        ):
            print("* ", end="")
        else:
            print("  ", end="")
    print()
