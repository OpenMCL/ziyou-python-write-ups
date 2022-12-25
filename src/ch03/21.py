n = int(input("> "))

max_height = 4 + 3 * n  # 3 (foot) + n (wall) + 2 * n + 1 (roof)

for row in range(max_height, 0, -1):
    row_output = ""
    for house in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
        house_height = 4 + 3 * house
        house_width = 1 + house * 4

        # Margin between houses
        if row_output:
            row_output += " "

        # Above the house
        if row > house_height:
            row_output += " " * house_width
            continue

        # Roof
        if row == house_height:
            row_output += " " * house * 2 + "*" + " " * house * 2
            continue
        elif row > 3 + house:
            roof_margin = row - 4 - house
            roof_width = house_width - 2 * roof_margin - 2
            row_output += "{0}/{1}\\{0}".format(" " * roof_margin, "-" * roof_width)
            continue

        # Wall
        if row > 3:
            wall_padding = house
            door_width = house_width - 2 - 2 * wall_padding

            # Door
            door = ""
            if door_width < 2 or row > 3 + house:
                door = " " * door_width
            elif row == 3 + house:
                door = " {} ".format("-" * (door_width - 2))
            else:
                door = "|{}|".format(" " * (door_width - 2))

            row_output += "|{0}{1}{0}|".format(" " * wall_padding, door)
            continue

        # Foot
        if row == 3:
            row_output += "|{}|".format("=" * (house_width - 2))
        else:
            row_output += "II{}II".format(" " * (house_width - 4))

    print(row_output)
