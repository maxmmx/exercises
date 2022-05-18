mode = input("Please input interface mode (access/trunk): ")
intrf = input("Please input interface name (example: Fa0/6): ")
vlans = input("Please input vlan(s) numbers (example 5 or 5,6,34): ")
access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable", ]
trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}", ]    
intconf = {"access": access_template, "trunk": trunk_template}
print("interface " + intrf) 
# print(str(intconf[mode]).replace("['", "").replace("'", "").replace(", ", "\n").replace("]'", "").format(vlans))
print("\n".join(intconf[mode]).format(vlans))

