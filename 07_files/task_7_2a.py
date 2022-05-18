ignore = ["duplex", "alias", "configuration"]
ignore_set = set(ignore)
with open("config_SW1.txt", "r") as f:
    for line in f:
        line_set = set(line.rstrip().split())
        if not (line.startswith("!") or ignore_set.intersection(line_set)):
            print(line.rstrip())

