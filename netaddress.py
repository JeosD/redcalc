import ipaddress

def calculared(net):
    try:
        netadd = ipaddress.ip_network(net, strict=False)
        mask = netadd.netmask
        wcard = netadd.hostmask
        bcast = netadd.broadcast_address
        if(str(mask)=="255.255.255.255"):
            bcast = None
            fstadd = netadd.network_address
            lstadd = netadd.network_address
            iptotal = netadd.num_addresses
            ipvalid = netadd.num_addresses
            return print("IP address: \t",net), print("Network address:",netadd), print("Netmask: \t",mask), print("Broadcast: \t",bcast), print("First host IP: \t",fstadd), print("Last host IP: \t",lstadd), print("Wild card: \t",wcard),print("Total IPs: \t",iptotal),print("IPs de host: \t",ipvalid)
        elif(str(mask)=="255.255.255.254"):
            fstadd = bcast-1
            lstadd = bcast
            iptotal = netadd.num_addresses
            ipvalid = netadd.num_addresses
            return print("IP address: \t",net), print("Network address:",netadd), print("Netmask: \t",mask), print("Broadcast: \t",bcast), print("First host IP: \t",fstadd), print("Last host IP: \t",lstadd), print("Wild card: \t",wcard),print("Total IPs: \t",iptotal),print("IPs de host: \t",ipvalid)
        elif(str(mask)=="0.0.0.0"):
            fstadd = mask
            lstadd = bcast
            iptotal = 0
            ipvalid = 0
            return print("IP address: \t",net), print("Network address:",netadd), print("Netmask: \t",mask), print("Broadcast: \t",bcast), print("First host IP: \t",fstadd), print("Last host IP: \t",lstadd), print("Wild card: \t",wcard),print("Total IPs: \t",iptotal),print("IPs de host: \t",ipvalid)
        else:
            fstadd = netadd[1]
            lstadd = netadd[-2]
            iptotal = netadd.num_addresses
            ipvalid = iptotal-2
            return print("IP address: \t",net), print("Network address:",netadd), print("Netmask: \t",mask), print("Broadcast: \t",bcast), print("First host IP: \t",fstadd), print("Last host IP: \t",lstadd), print("Wild card: \t",wcard),print("Total IPs: \t",iptotal),print("IPs de host: \t",ipvalid)
    except ValueError:
        return print("Invalid network address or subnet mask \nTry again...........")