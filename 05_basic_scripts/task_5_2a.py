net = input("Please enter network and maks x.x.x.x/y: ")
ip, mask = net.split("/")
ip_list = ip.split(".")
mask = int(mask)
oct1, oct2, oct3, oct4 = [
        int(ip_list[0]),
        int(ip_list[1]),
        int(ip_list[2]),
        int(ip_list[3])]
ip_bin = "{0:08b}{1:08b}{2:08b}{3:08b}".format(oct1, oct2, oct3, oct4)
ip_netw = ip_bin[0:mask] + "0" * (32 - mask)
mask_bin = "1" * mask + "0" * (32 - mask)
net1, net2, net3, net4 = [
    int(ip_netw[0:8], 2),
    int(ip_netw[8:16], 2), 
    int(ip_netw[16:24], 2), 
    int(ip_netw[24:32], 2) ]
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
print(output_net.format(net1, net2, net3, net4))
print(output_m.format(m1, m2, m3, m4, mask))

