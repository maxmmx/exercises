with open("ospf.txt", "r") as f:
    ospf_txt = f.readlines()
for string in ospf_txt:
    leng = len(string) - 1
    print("="*leng)
    print(string.strip())
    string = string.replace("[", "").replace("]", "").replace(",", "").split()
    print(f"{'Prefix':20}{string[1]}")
    print(f"{'AD/Metric':20}{string[2]}")
    print(f"{'Next-Hop':20}{string[4]}")
    print(f"{'Last update':20}{string[5]}")
    print(f"{'Outbound Interface':20}{string[6]}")
