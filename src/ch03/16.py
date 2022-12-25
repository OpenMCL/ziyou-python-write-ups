n = int(input())
for i in range(7):
    for _ in range(n):
        for j in range(5):
            if j == 2 or i == 2 or i == 4 or (i == 3 and (j == 0 or j == 4)):
                print("央" * n, end="")
            else:
                print("  " * n, end="")
        print()
