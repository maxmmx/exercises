mac_list = []
with open("CAM_table.txt", "r") as f:
    for line in f:
        if line.strip() and line.strip().split()[0].isdigit():
            line_list = line.rstrip().split()
            mac_list.append([int(line_list[0]), line_list[1], line_list[3]]) 
for list in sorted(mac_list):
    print(f"{list[0]:<8}{list[1]:20}{list[2]}")
vlan = input("Please input vlan number: ")
for vlan_s in mac_list:
    if int(vlan) == vlan_s[0]:
        print(f"{vlan_s[0]:<8}{vlan_s[1]:20}{vlan_s[2]}")

