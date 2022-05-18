mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
for mac_item in mac:
    result.append(mac_item.replace(":", "."))
print(f"Initial mac address: {mac}")
print(f"Cisco MAC address: {result}")
