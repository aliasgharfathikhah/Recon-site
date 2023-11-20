import socket

def Find_Port(url):
    url1 = url.replace("http://", "").replace("https://", "").replace("www.", "").replace("/", "")
    port_list = []
    hostname = url1
    print(url1)
    ip_address = socket.gethostbyname(hostname)
    common_ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 993, 995]

    for port in common_ports:  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            port_list.append("{}".format(port))
        else:
            pass
        sock.close()
    return port_list
