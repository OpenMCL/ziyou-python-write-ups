factor = [2, 3, 5, 7, 11]

for i in range(2, 100):
    temp = i
    print(temp, "=", end=" ")
    for fac in range(2, i + 1):
        while temp % fac == 0:
            temp = temp / fac
            if temp == 1:
                print(fac)
                break
            else:
                print(fac, end=" x ")
