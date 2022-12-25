n = int(input("> "))
c = 1
for i in range(n):
    print(str(i + 1) + "! =", end=" ")
    for j in range(i):
        print(str(j + 1) + "x", end="")
    print(str(i + 1) + " = " + str(c))
    c *= i + 2
