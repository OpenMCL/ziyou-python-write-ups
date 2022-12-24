n = int(input())
for i in range(n):
    for k in range(n):
        print(" " * n * (n - i - 1), end="")
        for w in range(2):
            for j in range(n - 1 if w == 0 else n):
                if i >= j:
                    print(
                        " " * (n - k - 1)
                        + str(k + 1) * (2 * k + 1)
                        + " " * (n - k - 1),
                        end=" ",
                    )
                else:
                    print(" " * (n * 2 - 1), end=" ")
        print()
