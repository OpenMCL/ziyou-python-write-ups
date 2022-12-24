n = int(input())
for i in range(3):
    for k in range(n):
        for j in range(3):
            s = int(3 / 2 * i + j / 2) + 1
            if i == j or i + j == 2:
                if k == 0 or k == n - 1:
                    print(str(s) * n, end="")
                else:
                    print(str(s) + " " * (n - 2) + str(s), end="")
            else:
                print(" " * n, end="")
        print()
