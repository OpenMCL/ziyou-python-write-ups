n = int(input("> "))
for i in range(n):
    for _ in range(n):
        print(" " * i + "\\" + " " * 2 * (n - i - 1) + "/" + " " * i, end="")
    print()
