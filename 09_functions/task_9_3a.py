from pprint import pprint
def get_int_vlan_map(config_filename):
    with open(config_filename, "r") as file:
        int_trunk = {}
        int_access = {}
        for line in file:
            if "interface" in line and "Vlan" not in line:
                int_name = line.strip().split()[-1]
            elif "switchport mode access" in line:
                spma = True            
            elif "switchport trunk allowed vlan" in line:
                int_trunk[int_name] = line.strip().split()[4:]
            elif "switchport access vlan" in line:
                int_access[int_name] = line.strip().split()[3]
                spma = False
            elif "duplex" in line and spma == True:
                int_access[int_name] = 1
                spma = False
    pprint(int_trunk)
    pprint(int_access)
    return int_trunk, int_access    
        
get_int_vlan_map("config_SW2.txt")
