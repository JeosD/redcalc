import ipaddress

red = str(input("Ingresa la IP a calcular: "))
print(type(red))
netadd = ipaddress.ip_network(red, strict=False)
mask = netadd.netmask
wcard = netadd.hostmask
bcast = netadd.broadcast_address
#fstadd = netadd[1]
#lstadd = netadd[-2]
iptotal = netadd.num_addresses
ipvalid = iptotal-2
print(netadd)