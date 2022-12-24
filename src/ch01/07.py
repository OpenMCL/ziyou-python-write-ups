n = int(input())
k = 1
for i in range(n):
    print(" " * (n - i - 1) * 2, end="")
    for j in range(i + 1):
        print(k % 10, end=" ")
        k += 1
    print()
