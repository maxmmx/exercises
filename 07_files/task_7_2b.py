import sys 
# print(sys.argv[0])
# print(sys.argv[1])
ignore = ["duplex", "alias", "configuration"]
ignore_set = set(ignore)
with open(sys.argv[1], "r") as f:
	with open(sys.argv[2], "w") as w:
		for line in f:
			line_set = set(line.rstrip().split())
			if not (line.startswith("!") or ignore_set.intersection(line_set)):
				w.write(line)



