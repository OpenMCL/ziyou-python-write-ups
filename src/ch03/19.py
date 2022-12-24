n = int(input())
for i in range(n * 2 + 1 + n + 1):
    for j in range(n):
        for k in range(2):
            h = n * 3 - i
            w = n - j - 1
            h2 = h - w - 1
            if h <= w and h >= 0:
                print(" " * (w + 1) * 2 + "|" + " " * (w + 1) * 2, end=" ")
            elif h < 0:
                print("=" * ((w + 1) * 4 + 1), end="=")
            elif h2 >= 0 and h2 < (w * 2 + 3):
                print(" " * h2 + "*" * ((2 * (w + 1) - h2) * 2 + 1) + " " * h2, end=" ")
            else:
                print(" " * ((w + 1) * 4 + 1), end=" ")
    print()
