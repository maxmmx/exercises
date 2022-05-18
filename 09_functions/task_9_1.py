def generate_access_config(intf_vlan_mapping, access_template):
    result = []
    for key in intf_vlan_mapping:
        result.append(f"interface {key}")
        for string in access_mode_template:
            if string.endswith("vlan"):
                result.append(f"{string} {(intf_vlan_mapping[key])}")
            else:
                result.append(string)
    return result
    

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}
print(generate_access_config(access_config, access_mode_template))
print("="*40)
print(generate_access_config(access_config_2, access_mode_template))

