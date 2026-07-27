import socket
import re
import argparse


parser = argparse.ArgumentParser()

args = parser.add_argument("-ip", "--ip", help='Set ip, example: -ip 192.168.0.100', type=str)
args = parser.add_argument("-l", "--list", help="Specify list ip, example: -l ips.txt", type=str)
args = parser.add_argument("-p", "--port", help="Specify port to scan, example: -p 22", nargs="+", type=str)
args = parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 2", type=int)

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
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(10)
    result = s.connect_ex((ip, port))
    s.close()
    return result

def scan_port(ip, port):
    if args.ip:
        try:
            result = requests(ip, int(port[0]))
            if result == 0:
                print(f"\033[92mOpen: {port[0]}\033[00m")
        except:
            pass
    elif args.list:
        file = open(args.list, encoding="utf-16").read().splitlines()
        for ips in file:
            try:
                result = requests(ips, int(port[0]))
                print(f"===== {ips} =====")
                if result == 0:
                    print(f"\033[92mOpen: {port[0]}\033[00m")
            except:
                pass

def scan_multiples_ports(ip, port):
    regex_ports = re.findall(r"(\d+)(?:-(\d+))?", port)
    start_port = int(regex_ports[0][0])
    end_port = int(regex_ports[0][1])

    for ports in range(start_port, end_port+1):
        if args.ip:
            try:
                result = requests(ip, ports)
                if result == 0:
                    print(f"\033[92mOpen: {ports}\033[00m")
            except:
                pass
        elif args.list:
            file = open(args.list, encoding="utf-16").read().splitlines()
            for ips in file:
                try:
                    result = requests(ips, ports)
                    if result == 0:
                        print(f"\033[92mOpen: {ports}\033[00m")
                except:
                    pass

if __name__ == "__main__":
    main()