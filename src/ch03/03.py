n = int(input())
for i in range(n):
    for k in range(n):
        print(" " * n * (n - i - 1), end="")
        for w in range(2):
            for j in range(n - 1 if w == 0 else n):
                if i >= j:
                    if k == 0 or k == n - 1:
                        print(
                            " " * (n - k - 1)
                            + str(k + 1) * (2 * k + 1)
                            + " " * (n - k - 1),
                            end=" ",
                        )
                    else:
                        print(
                            " " * (n - k - 1)
                            + str(k + 1)
                            + " " * (2 * k - 1)
                            + str(k + 1)
                            + " " * (n - k - 1),
                            end=" ",
                        )
                else:
                    print(" " * (n * 2 - 1), end=" ")
        print()
for i in range(n - 1, -1, -1):
    for k in range(n - 2 if i == n - 1 else n - 1, -1, -1):
        print(" " * n * (n - i - 1), end="")
        for w in range(2):
            for j in range(n - 1 if w == 0 else n):
                if i >= j:
                    if k == 0 or k == n - 1:
                        print(
                            " " * (n - k - 1)
                            + str(k + 1) * (2 * k + 1)
                            + " " * (n - k - 1),
                            end=" ",
                        )
                    else:
                        print(
                            " " * (n - k - 1)
                            + str(k + 1)
                            + " " * (2 * k - 1)
                            + str(k + 1)
                            + " " * (n - k - 1),
                            end=" ",
                        )
                else:
                    print(" " * (n * 2 - 1), end=" ")
        print()
