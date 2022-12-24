p = "呆秀才吃長齋鬍鬚滿腮經書揭不開紙筆自己安排明年不請我自來"
p1 = [["  "] * (i + 1) for i in range(7)]
r, s = 6, 0
k = 0
for i in p:
    p1[r][s] = i
    if r == 6:
        r = 5 - s
        s = 0
    else:
        r += 1
        s += 1
for i in range(7):
    print("  " * (7 - i), end="")
    for j in range(i + 1):
        print(p1[i][j], end="  ")
    print("  " * (7 - i) + "  " * 3 + "  " * (7 - i), end="")
    for j in range(i, -1, -1):
        print(p1[i][j], end="  ")

    print()
