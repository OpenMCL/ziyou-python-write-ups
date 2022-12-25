n = int(input("> "))

for i in range(1, n * 2 + 1):
    for j in range(1, (n * 2 - 3) * 2 + 1):
        if j <= 2 or j >= ((n * 2 - 3) * 2 - 1):
            print("M", end="")
        elif i >= 2 and i <= n * 2 - 2 and j <= (n * 2 - 3) * 2:
            if i - j + 2 > 0 and i - j + 2 <= 3 and j <= (n * 2 - 3):
                print("M", end="")
            elif (
                (i - ((n * 2 - 3) * 2 + 1 - j) + 2) > 0
                and (i - ((n * 2 - 3) * 2 + 1 - j) + 2) <= 3
                and j >= (n * 2 - 3)
            ):
                print("M", end="")
            else:
                print(" ", end="")
        else:
            print(" ", end="")
    print()
