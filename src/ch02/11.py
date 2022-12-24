n = int(input())
for i in range(n - 1):
    for j in range(n):
        print(" " * (n - i - 1) + "/" + "||" * i + "\\" + " " * (n - i - 2), end="")
    print()
print("x", end="")
for j in range(n):
    print("||" * (n - 1) + "x", end="")
print()
for i in range(n - 2, -1, -1):
    for j in range(n):
        print(" " * (n - i - 1) + "\\" + "||" * i + "/" + " " * (n - i - 2), end="")
    print()
