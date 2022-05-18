from pprint import pprint
def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result = []
    result_dict = {}
    for key, value in intf_vlan_mapping.items():
        #result.append(f"interface {key}")
        for string in trunk_template:
            if string.endswith("vlan"):
                vlans_str = ",".join(str(vlan_num) for vlan_num in value) 
                result.append(f"{string} {vlans_str}")
            else:
                result.append(f"{string}")
        result_dict[key] = result
    return result_dict


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}

pprint(generate_trunk_config(trunk_config, trunk_mode_template))
print("f"*40)
pprint(generate_trunk_config(trunk_config_2, trunk_mode_template))
