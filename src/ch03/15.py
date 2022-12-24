n = int(input())

for k in range(5):
    for j in range(5):
        for i in range(n):
            if k == 1 and i != n - 1:
                print(" " * n, end=" ")
            elif k == 3 and i != 0:
                print(" " * n, end=" ")
            elif j % 2 == 0:
                print("2" * n, end=" ")
            elif j == 1:
                print(" " * (n - 1), end="")
                print("2", end=" ")
            elif j == 3:
                print("2", end="")
                print(" " * (n - 1), end=" ")
        print()
