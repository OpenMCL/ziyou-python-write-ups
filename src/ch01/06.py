n = int(input())
a = 4 * (n - 1)
b = n + 1
c = 3 * (n - 1) + 1
for i in range(n):
    print((i + 1) % 10, end=" ")
print()
for i in range(n - 2):
    print(str(a % 10) + " " + " " * (n - 2) * 2 + str(b % 10))
    a -= 1
    b += 1
for i in range(n):
    print(c % 10, end=" ")
    c -= 1
