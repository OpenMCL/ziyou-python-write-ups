n = int(input())
hh, vv = chr(9472), chr(9474)
nw, ne, sw, se = chr(9484), chr(9488), chr(9492), chr(9496)

m = (n - 1) / 2
for i in range(n):
    for j in range(n):
        if i == j:
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
    print()
