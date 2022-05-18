net = input("Please enter network and maks x.x.x.x/y: ")
ip, mask = net.split("/")
ip_list = ip.split(".")
mask = int(mask)
oct1, oct2, oct3, oct4 = [
        int(ip_list[0]),
        int(ip_list[1]),
        int(ip_list[2]),
        int(ip_list[3])]
mask_bin = "1" * mask + "0" * (32 - mask)
m1, m2, m3, m4 = [
    int(mask_bin[0:8], 2),
    int(mask_bin[8:16], 2), 
    int(mask_bin[16:24], 2), 
    int(mask_bin[24:32], 2) ]
output_net = """
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:>08b} {1:>08b} {2:>08b} {3:>08b}
"""
output_m = """

Mask:
/{4}
{0:<8} {1:<8} {2:<8} {3:<8}
{0:>08b} {1:>08b} {2:>08b} {3:>08b}
"""
print(output_net.format(oct1, oct2, oct3, oct4))
print(output_m.format(m1, m2, m3, m4, mask))

