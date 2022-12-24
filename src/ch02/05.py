for i in range(1, 10):
    # 1   1   1 ...  1   1
    print(("  " + str(i) + "  ") * 9)

    # x 1  x 2 ... x 9
    for j in range(1, 10):
        print("x " + str(j) + "  ", end="")
    print()

    # --- --- ... ---
    print("---  " * 9)

    # 1   2   3 ... 9
    for j in range(1, 10):
        space = " " if (i * j) // 10 else "  "
        print(space + str(i * j) + "  ", end="")
    print()

    # blank line
    print()
