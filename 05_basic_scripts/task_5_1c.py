london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}
eqName = input("Please type name of equipment (r1/r2/sw1): ")
# eqParamStrAll = str(list(london_co.get(eqName).keys())).replace("[", "").replace("]", "").replace("'", "")
eqParamStrAll = ", ".join(london_co[eqName].keys())
# eqParam = input("Please type parameter of " + eqName + " (" + eqParamStrAll + "): ")
eqParam = input(f"Please type parameter of {eqName} ({eqParamStrAll}): ")
# print(london_co[eqName].pop(eqParam, "No such parameter"))
print(london_co[eqName].get(eqParam, "No such parameter"))
