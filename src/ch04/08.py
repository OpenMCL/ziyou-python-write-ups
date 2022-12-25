n = int(input("> "))

prev_row = []
for _ in range(n + 1):
    # Compute the Pascal's triangle
    if len(prev_row) == 0:
        row = [1]
    else:
        row = [1]
        for i in range(1, len(prev_row)):
            row.append(prev_row[i - 1] + prev_row[i])
        row.append(1)

    # Left margin
    print(" " * 2 * (n - len(row) + 1), end=" ")

    # The triangle
    for val in row:
        print("{:>3}".format(val), end=" ")
    print()

    prev_row = row
