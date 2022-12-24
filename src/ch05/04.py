import random

kid = [(28, 62, 28, 8, 28, 62, 93, 28, 20, 20), (28, 62, 93, 8, 28, 62, 93, 28, 62, 20)]

kids = [random.randint(0, 1) for x in range(random.randint(3, 10))]
for j in range(10):
    for i in range(len(kids)):
        a = kids[i]
        for k in range(6, -1, -1):
            if (kid[a][j] >> k) % 2:
                if a == 0:
                    if j < 3:
                        print("*", end="")
                    elif j == 3:
                        print("I", end="")
                    elif 3 < j < 8 and 1 < k < 5:
                        print((i + 1) % 10, end="")
                    elif j > 7:
                        print("|", end="")
                    elif k < 2:
                        print("\\", end="")
                    else:
                        print("/", end="")
                else:
                    if j < 3 and 0 < k < 6:
                        print("*", end="")
                    elif j == 3:
                        print("I", end="")
                    elif 3 < j < 7 and 1 < k < 5:
                        print((i + 1) % 10, end="")
                    elif 6 < j < 9:
                        print("*", end="")
                    elif j == 9:
                        print("|", end="")
                    elif k < 2:
                        print("\\", end="")
                    else:
                        print("/", end="")
            else:
                print(" ", end="")

    print()
