n = int(input())
# 屋頂
for i in range(2 * n + 1):
    if i == 0:
        for j in range(5):
            if j % 2 == 0:
                print(" " * (2 * n - i) + "*" + " " * (2 * n - i), end=" ")
            else:
                print(" " * (4 * n - 3), end=" ")
        print()
    elif i == 1 or i == 2:
        for j in range(5):
            if j % 2 == 0:
                print(
                    " " * (2 * n - i)
                    + "/"
                    + "-" * (2 * i - 1)
                    + "\\"
                    + " " * (2 * n - i),
                    end=" ",
                )
            else:
                print(" " * (4 * n - 3), end=" ")
        print()
    elif i == 3:
        for j in range(5):
            if j % 2 == 0:
                print(
                    " " * (2 * n - i)
                    + "/"
                    + "-" * (2 * i - 1)
                    + "\\"
                    + " " * (2 * n - i),
                    end=" ",
                )
            else:
                print(" " * (2 * n - i + 1) + "*" + " " * (2 * n - i + 1), end=" ")
        print()
    else:
        for j in range(5):
            if j % 2 == 0:
                print(
                    " " * (2 * n - i)
                    + "/"
                    + "-" * (2 * i - 1)
                    + "\\"
                    + " " * (2 * n - i),
                    end=" ",
                )
            else:
                print(
                    " " * (2 * n - i + 1)
                    + "/"
                    + "-" * (2 * i - 7)
                    + "\\"
                    + " " * (2 * n - i + 1),
                    end=" ",
                )
        print()
# 門
for i in range(n):
    if i == 0:
        for j in range(5):
            if j % 2 == 0:
                print(
                    "|" + " " * (n + 1) + "_" * (2 * n - 3) + " " * (n + 1) + "|",
                    end=" ",
                )
            else:
                print("/" + "-" * (4 * n - 5) + "\\", end=" ")
        print()
    elif i == 1:
        for j in range(5):
            if j % 2 == 0:
                print(
                    "|" + " " * n + "|" + " " * (2 * n - 3) + "|" + " " * n + "|",
                    end=" ",
                )
            else:
                print("|" + " " * n + "_" * (2 * n - 5) + " " * n + "|", end=" ")
        print()
    else:
        for j in range(5):
            if j % 2 == 0:
                print(
                    "|" + " " * n + "|" + " " * (2 * n - 3) + "|" + " " * n + "|",
                    end=" ",
                )
            else:
                print(
                    "|"
                    + " " * (n - 1)
                    + "|"
                    + " " * (2 * n - 5)
                    + "|"
                    + " " * (n - 1)
                    + "|",
                    end=" ",
                )
        print()
# 地板
for i in range(5):
    if i % 2 == 0:
        print("|" + "=" * (4 * n - 1) + "|", end=" ")
    else:
        print("|" + "=" * (4 * n - 5) + "|", end=" ")
print()
# 腳
for i in range(2):
    for j in range(5):
        if j % 2 == 0:
            print("II" + " " * (4 * n - 3) + "II", end=" ")
        else:
            print("II" + " " * (4 * n - 7) + "II", end=" ")
    print()
