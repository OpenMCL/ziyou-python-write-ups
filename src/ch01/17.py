n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(str(j + 1) * n, end=" ")
    print()
