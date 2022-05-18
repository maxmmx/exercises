with open("config_SW1.txt", "r") as f:
    for line in f:
        if not line.startswith("!" or "\n"):
            print(line.rstrip())

