mode = input("Please input interface mode (access/trunk): ")
intrf = input("Please input interface name (example: Fa0/6): ")
quest_acc = "Please input vlan number (example 5): "
quest_trunk = "Please input vlan(s) numbers (example 5 or 5,6,34):" 
quest = {"access": quest_acc, "trunk": quest_trunk}
vlans = input(quest[mode])
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
print("\n".join(intconf[mode]).format(vlans))

