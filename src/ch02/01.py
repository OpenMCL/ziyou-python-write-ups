t = 0
for i in range(100, 1000):
    if i // 100 != (i % 100) // 10 and (i % 100) // 10 != i % 10 and i // 100 != i % 10:
        if i // 100 + (i % 100) // 10 + i % 10 == 10:
            t += 1

print(t)
