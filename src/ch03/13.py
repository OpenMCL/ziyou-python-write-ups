n = int(input("> "))

for i in range(1, n * 2 + 1):
    for j in range(1, (n * 2 - 3) * 2 + 1):
        if j <= 2 or j >= ((n * 2 - 3) * 2 - 1):
            print("M", end="")
        elif i >= 3 and i <= n * 2 - 2:
            if (i - 1) // 2 + 2 == (j - 1) // 2 + 2 or (
                (n * 2 - 3) * 2 - j
            ) // 2 + 2 == (i - 1) // 2 + 2:
                print("M", end="")
            else:
                print(" ", end="")
        else:
            print(" ", end="")
    print()
