import socket
from IPy import IP



def  scan(target,prt_num):
    converted_ip = check_ip(target)
    print('\n'+'[ [+] Scanning Target ] ' + str(target))
    for port in range(1, prt_num):
     scan_port(converted_ip, port)

def  check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def  get_banner(s):
    return s.recv(1024)

def  scan_port(ipaddress, port):    # to scan ports
    try:
        sock = socket.socket()# rem
        sock.settimeout(0.5) # sets time out
        sock.connect((ipaddress, port))
        try:
             ban = get_banner(sock)
             print("[+] Open port" + str(port) + ":" + str(ban.decode().strip('\n')))

        except:

            print("[+] Open port" + str(port))
    except:
           pass

    #banner will give which os are running on the device and what is happening

if __name__ == "__main__":
    ipaddress = input("Enter the ipaddress:\n")
    port_num = int(input("Enter the number of ports you want to scan \n "))

    if ',' in ipaddress:
        for ip_address in ipaddress.split(', '):
            scan(ip_address.strip(' '), port_num)
    else:
        scan(ipaddress, port_num)




