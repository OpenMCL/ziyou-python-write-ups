for i1 in range(1, 10):
    for i2 in range(10):
        for i3 in range(10):
            if (
                ((i1 * 10000 + i2 * 1000 + i3 * 100 + i1 * 10 + i2) * i1) % 111111
            ) == 0:
                print(i1 * 10000 + i2 * 1000 + i3 * 100 + i1 * 10 + i2)
