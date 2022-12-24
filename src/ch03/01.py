n = int(input())
for i in range(n):
    for k in range(n):
        print(" " * n * (n - i - 1), end="")
        for j in range(i + 1):
            if k == 0 or k == n - 1:
                print(
                    " " * (n - k - 1) + str(j + 1) * (2 * k + 1) + " " * (n - k - 1),
                    end=" ",
                )
            else:
                print(
                    " " * (n - k - 1)
                    + str(j + 1)
                    + " " * (2 * k - 1)
                    + str(j + 1)
                    + " " * (n - k - 1),
                    end=" ",
                )
        print()
