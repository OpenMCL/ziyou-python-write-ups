import numpy as np

n = int(input("> "))

# Alias
_2n = 2 * n
_3n = 3 * n
_4n = 4 * n
_5n = 5 * n
_8n = 8 * n
range_n_1 = range(n + 1)
range_n_2 = range(n + 2)

# Prepare a 2D grid
rows = _3n + 10
cols = _8n + 25
grid = np.array([[" " for _ in range(cols)] for _ in range(rows)], dtype=str)

# Back
grid[1, [4 + _2n + i for i in range(6 + _2n)]] = "_"
grid[[2 + i for i in range_n_2], [_2n + 3 - i for i in range_n_2]] = "/"
grid[[4 + n + i for i in range_n_2], n + 2] = "|"

# Tail
grid[[_2n + 6 + i for i in range_n_2], [n + 2 - i for i in range_n_2]] = "/"
grid[-2, 0] = "*"

# Legs
for col_idx in [4 + n, _4n + 12]:
    grid[[7 + _2n + i for i in range(n + 3)], col_idx] = "I"
    grid[[7 + _2n + i for i in range(n + 3)], col_idx + n + 3] = "I"
    grid[-1, [col_idx + 1 + i for i in range(n + 2)]] = "_"

# Bottom
grid[_2n + 6, n + 3] = "\\"
grid[_2n + 6, [_2n + 8 + i for i in range(4 + _2n)]] = "_"
grid[_2n + 6, _5n + 16] = "/"
grid[_2n + 5, _5n + 16] = "|"
grid[_2n + 4, [_5n + 17 + i for i in range(3 + _2n)]] = "_"

# Nose
grid[[_2n + 5 + i for i in range(n + 2)], [-5 - n + i for i in range(n + 2)]] = "\\"
grid[[-3, -2], -3] = "|"
grid[-1, -3:] = ":"
grid[-(n + 3) : -1, -1] = "|"
grid[[1 + i for i in range(6 + _2n)], [-7 - _2n + i for i in range(6 + _2n)]] = "\\"

# Head
grid[0, [-8 - _2n - i for i in range(7 + _2n)]] = "_"
grid[[1 + i for i in range_n_2], [-15 - _4n - i for i in range_n_2]] = "/"
grid[[3 + n + i for i in range_n_2], [-16 - _5n + i for i in range_n_2]] = "\\"
grid[4 + _2n, [-14 - _4n + i for i in range(3)]] = "_"
grid[[4 + _2n - i for i in range_n_1], [[13 + _4n + i for i in range_n_1]]] = "/"

# Eye
grid[3 + n, 17 + _5n] = "@"

print("\n".join(["".join(row) for row in grid]))
