n = int(input("> "))
for i in range(3):
    for k in range(n):
        for j in range(3):
            if i == j or i + j == 2:
                if k == int(n / 2):
                    print(" " * int(n / 2) + "X" + " " * int(n / 2), end="")
                elif k < int(n / 2):
                    print(
                        " " * k
                        + "\\"
                        + " " * ((int(n / 2) - k) * 2 - 1)
                        + "/"
                        + " " * k,
                        end="",
                    )
                else:
                    print(
                        " " * (n - k - 1)
                        + "/"
                        + " " * ((k - int(n / 2)) * 2 - 1)
                        + "\\"
                        + " " * (n - k - 1),
                        end="",
                    )
            else:
                print(" " * n, end="")
        print()
