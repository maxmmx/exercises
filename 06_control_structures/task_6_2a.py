ip = input("Please enter IP address in dec (aka 10.1.1.1) format: ")
octets = ip.split(".")
ip_check = False
if len(octets) == 4:
    ip_check = True
for octs in octets:
    if octs.isdecimal() == False:
        ip_check = False
    elif not(0 <= int(octs) <= 255):
        ip_check = False
if ip_check == False:
    print("IP Address is wrong")
else:
    if int(octets[0]) < 224 and int(octets[0]) > 0:
        print("Unicast")
    elif int(octets[0]) < 240 and int(octets[0]) > 223:
        print("Multicast")
    elif int(octets[0]) == 255 and int(octets[1]) == 255 and int(octets[2]) == 255 and int(octets[3]) == 255: 
        print("Broadcast")
    elif int(octets[0]) == 0 and int(octets[1]) == 0 and int(octets[2]) == 0 and int(octets[3]) == 0:
        print("Default")
    else: print("Unused")

