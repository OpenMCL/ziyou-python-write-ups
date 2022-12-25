n = int(input("> "))
hh, vv = chr(9472), chr(9474)
nw, ne, sw, se = chr(9484), chr(9488), chr(9492), chr(9496)

for i in range(2 * n - 1):
    for j in range(n):
        if j - i >= 1 or i - j >= n:
            print(" " * 5, end=" ")
        else:
            if i - j == 0:
                print(nw + hh * 3 + ne, end=" ")
            elif i - j == n - 1:
                print(sw + hh * 3 + se, end=" ")
            else:
                print(vv + hh * 3 + vv, end=" ")
    print()
