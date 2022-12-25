import random

n = int(input("> "))

ran = [x for x in range(-n + 1, n)]
random.shuffle(ran)
for i in range(3 * n + 1, 0, -1):
    for j in ran:
        s = abs(j)
        d = 3 * s
        h = 3 * n + 1 - d
        f = n - s
        w = 4 * (n - s) + 1
        if i > h:
            print(" " * w, end=" ")
        elif h >= i > f:
            print(
                " " * (i - f - 1)
                + "*" * ((((n - s) * 2 + 1) - (i - f - 1)) * 2 - 1)
                + " " * (i - f - 1),
                end=" ",
            )
        else:
            print(" " * (2 * f) + "|" + " " * (2 * f), end=" ")
    print()
print("=" * (4 * n * n + 4 * n - 3))
