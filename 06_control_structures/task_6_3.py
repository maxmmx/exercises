access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {
    "0/1": ["add", "10", "20"],
    "0/2": ["only", "11", "30"],
    "0/4": ["del", "17"],
    "0/5": ["add", "10", "21"],
    "0/7": ["only", "30"],
}

for port in trunk:
    print(f"interface FastEthernet{port}")
    for line in trunk_template:
        if line.endswith("vlan"):
            if trunk[port][0] == "del":
                trunk[port].remove("del")
                vlans_str = ",".join(trunk[port])
                print(f" {line} remove {vlans_str}")
            elif trunk[port][0] == "only":
                trunk[port].remove("only")
                vlans_str = ",".join(trunk[port])
                print(f" {line} {vlans_str}")
            else:
                trunk[port].remove("add")
                vlans_str = ",".join(trunk[port])
                print(f" {line} add {vlans_str}")
        else:
            print(f" {line}")

# for intf, vlan in access.items():
#     print("interface FastEthernet" + intf)
#     for command in access_template:
#         if command.endswith("access vlan"):
#             print(f" {command} {vlan}")
#         else:
#             print(f" {command}")

