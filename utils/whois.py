import socket

def get_whois(url):
    url1 = url.replace("http://", "").replace("https://", "").replace("www.", "").replace("/", "")
    if url1[-3:] == "org" or url1[-3:] == "com" or url1[-3:] == "net":
        whois_server = "whois.internic.net"
    else:
        whois_server =  "whois.iana.org"

    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((whois_server,43))
    s.send((url1+"\r\n").encode())

    msg = s.recv(10000)
    msg = msg.decode()
    msg = msg[137:]
    print(msg)
    return msg