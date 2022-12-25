n = int(input())
print("1 " * (n - 1) + "2")
for _ in range(n - 2):
    print("4 " + " " * 2 * (n - 2) + "2")
print("4 " + "3 " * (n - 1))
