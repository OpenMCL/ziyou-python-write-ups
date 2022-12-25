n = int(input())
for i in range(n):
    for _ in range(n):
        print(" " * (n - i - 1) + str(i + 1) * (2 * i + 1) + " " * (n - i - 1), end=" ")
    print()
