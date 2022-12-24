n = int(input())
c = int(n * (n + 1) / 2)
for i in range(n, 0, -1):
    print("sum([1," + str(i) + "]) =", end=" ")
    for j in range(i - 1):
        print(str(j + 1) + "+", end="")
    print(str(i) + " = " + str(c))
    c -= i
