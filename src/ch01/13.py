n = int(input("> "))
for i in range(n):
    for _ in range(n):
        print(" " * i + "\\" + " " * 2 * (n - i - 1) + "/" + " " * i, end="")
    print()
for i in range(n - 1, -1, -1):
    for _ in range(n):
        print(" " * i + "/" + " " * 2 * (n - i - 1) + "\\" + " " * i, end="")
    print()
