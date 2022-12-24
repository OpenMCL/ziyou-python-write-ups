n = int(input())
hh, vv = chr(9472), chr(9474)
nw, ne, sw, se = chr(9484), chr(9488), chr(9492), chr(9496)
nw1, ne1, sw1, se1 = se, sw, ne, nw
# print (sw)
m = (n - 1) / 2
for i in range(n):
    for j in range(n):
        if i == 0 and j == n - 1:
            print(hh + ne, end="")
        elif i == j:
            if i > m:
                print(se, end="")
            else:
                print(nw, end="")
        elif i + j == n - 1 and i > m:
            print(sw, end="")
        elif i + j == n and i <= m:
            print(ne, end="")
        elif i - j > 0 and i + j < n - 1:
            print(vv, end="")
        elif i - j < 0 and i + j > n:
            print(vv, end="")
        else:
            print(hh, end="")
    if i != 0 and i != n - 1:
        print(vv, end="")
    else:
        if i != 0 and i != n - 1:
            print(" ", end="")
    for j in range(n - 1, -1, -1):
        if i == n - 1 and j == n - 1:
            print(sw, end="")
        if (n - i - 1) == j:
            if (n - i - 1) > m:
                print(se1, end="")
            else:
                print(nw1, end="")
        elif (n - i - 1) + j == n - 1 and (n - i - 1) > m:
            print(sw1, end="")
        elif (n - i - 1) + j == n and (n - i - 1) <= m:
            print(ne1, end="")
        elif (n - i - 1) - j > 0 and (n - i - 1) + j < n - 1:
            print(vv, end="")
        elif (n - i - 1) - j < 0 and (n - i - 1) + j > n:
            print(vv, end="")
        else:
            print(hh, end="")
    print()
