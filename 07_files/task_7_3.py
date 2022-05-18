with open("CAM_table.txt", "r") as f:
    for line in f:
        if line.strip():
            line_list = line.strip().split()
            if line_list[0].isdigit():
                print(f"{line_list[0]:8}{line_list[1]:18}{line_list[3]}")

