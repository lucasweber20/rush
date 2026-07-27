import socket
import re
import argparse
from urllib.parse import urlsplit


parser = argparse.ArgumentParser()

args = parser.add_argument("-ip", "--ip", help='Set ip, example: -ip 192.168.0.100', type=str)
args = parser.add_argument("-l", "--list", help="Specify list ip, example: -l ips.txt", type=str)
args = parser.add_argument("-p", "--port", help="Specify port to scan, example: -p 22 or -p 1-100", nargs="+", type=str)

args = parser.parse_args()

def main():
    if args.ip:
        if "-" in args.port[0]:
            scan_multiples_ports(args.ip, args.port[0])
        scan_port(args.ip, args.port)
    elif args.list:
        if "-" in args.port[0]:
            scan_multiples_ports(args.ip, args.port[0])
        scan_port(args.list, args.port)

def requests(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(10)
        result = s.connect_ex((ip, port))
        s.close()
        return result
    except:
        pass

def read_file(file):
    hostnames = []
    urls = open(file, encoding="utf-8").read().splitlines()
    for url in urls:
        hostname_url = urlsplit(url)
        hostnames.append(hostname_url.netloc)
    return hostnames

def scan_port(ip, port):
    if args.ip:
        try:
            result = requests(ip, int(port[0]))
            if result == 0:
                print(f"\033[92mOpen: {port[0]}\033[00m")
        except:
            pass
    elif args.list:
        hostnames = read_file(args.list)
        for host in hostnames:
                result = requests(host, int(port[0]))
                print(f"===== {host} =====")
                if result == 0:
                    print(f"\033[92mOpen: {port[0]}\033[00m")

def scan_multiples_ports(ip, port):
    regex_ports = re.findall(r"(\d+)(?:-(\d+))?", port)
    start_port = int(regex_ports[0][0])
    end_port = int(regex_ports[0][1])

    for ports in range(start_port, end_port+1):
        if args.ip:
                result = requests(ip, ports)
                if result == 0:
                    print(f"\033[92mOpen: {ports}\033[00m")
        elif args.list:
                hostnames = read_file(args.list)
                for host in hostnames:
                        result = requests(host, ports)
                        if result == 0:
                            print(f"\033[92mOpen: {ports}\033[00m")

if __name__ == "__main__":
    main()