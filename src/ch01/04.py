n = int(input())
k = n
for i in range(n):
    print((i + 1) % 10, end=" ")
print()
for i in range(n - 2):
    print(str((k + 1) % 10) + " " * ((n - 2) * 2 + 1) + str((k + 2) % 10))
    k += 2
for i in range(n):
    print((k + 1) % 10, end=" ")
    k += 1
