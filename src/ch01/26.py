n = int(input())
for i in range(n):
    for j in range(n):
        print(" " * (n - i - 1) + "/\\" * (i + 1) + " " * (n - i - 1), end="")
    print()
print("-" * n * n * 2)
for i in range(n - 1, -1, -1):
    for j in range(n):
        print(" " * (n - i - 1) + "\\/" * (i + 1) + " " * (n - i - 1), end="")
    print()
