n = int(input())

for i in range(2 * n - 1):
    for j in range(n):
        if j - i >= 1 or i - j >= n:
            print(" " * n, end=" ")
        else:
            if i - j == n - 1:
                print(str(j + 1) * n, end=" ")
            else:
                print(str(j + 1) + " " * (n - 2) + str(j + 1), end=" ")
    print()
