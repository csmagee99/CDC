import os

ping = "ping "
open_ports = "nmap -Pn "
http_enum = "nmap -sV --script=http-enum "
os_detect = "nmap -O "
vuln_scan = "nmap -V --script vuln "
exploit = "nmap --script brute -Pn "
dos = "nmap --script dos -Pn "

def main():
    with open("domain_name", "r") as file:
        for ip in file:
            print('Website:' + ' ' + ip)
            os.system(open_ports + " " + ip)
main()
