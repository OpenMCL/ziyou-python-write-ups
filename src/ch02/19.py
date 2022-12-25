n = int(input())
hh, vv = chr(9472), chr(9474)
nw, ne, sw, se = chr(9484), chr(9488), chr(9492), chr(9496)

for i in range(-n, n + 1):
    for _ in range(n):
        for j in range(-n, n):
            if i + j <= -n - 2 or j - i > n or i - j > n + 1 or i + j > n:
                print(" " * (2), end="")
            else:
                if i + j == -n - 1:
                    print(nw + hh + se, end="") if i != -n else print(nw + hh, end="")
                elif j - i == n:
                    print(sw + hh + ne, end="") if i != -n else print(hh + ne, end="")
                elif i == 0 and j == -n:
                    print(vv + "  ", end="")
                elif i == 0 and j == n - 1:
                    print("  " + vv, end="")
                elif i - j == n + 1:
                    print(sw + hh + ne, end="") if i != n else print(sw + hh, end="")
                elif i + j == n:
                    print(nw + hh + se, end="") if i != n else print(hh + se, end="")
                else:
                    print(" ", end="") if j == 0 or j == -1 else print(" " * 2, end="")
    print()
