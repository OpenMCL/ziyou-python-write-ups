n = int(input("> "))
zd = [
    [0b00100, 0b11111, 0b10101, 0b11111, 0b00100],
    [0b00100, 0b11111, 0b00100, 0b01010, 0b10001],
]
zdw = ["中", "大"]
for c in range(2):
    for i in range(5):
        for m in range(n):
            for k in range(-n + 1, n):
                for j in range(5):
                    if (
                        i * n + m >= abs(k) * 5
                        and (zd[c][((i * n + m) - abs(k) * 5) // (n - abs(k))] >> j) % 2
                    ):
                        print(zdw[c] * (n - abs(k)), end="")
                    else:
                        print("  " * (n - abs(k)), end="")
                print(" ", end="")
            print()
