import socket
import argparse


parser = argparse.ArgumentParser()

args = parser.add_argument("-ip", "--ip", help='Set ip, example: -ip 192.168.0.100', type=str)
args = parser.add_argument("-l", "--list", help="Specify list ip, example: -l ips.txt", type=str)
args = parser.add_argument("-p", "--port", help="Specify port to scan, example: -p 22", type=int)
args = parser.add_argument("-o", "--output", help="Specify output file, example: -o outputs.txt", type=str)
args = parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 2", type=int)

args = parser.parse_args()

def main():
    if args.ip:
        result = scan(args.ip, args.port)
    elif args.list:
        result = scan(args.list, args.port)

def scan(ip, port):
    if args.ip:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"\033[92m{port} is open!!!\033[00m")
            s.close()
        except:
            pass
    elif args.list:
        file = open(args.list, encoding="utf-16").read().splitlines()
        for ips in file:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(5)
                result = s.connect_ex((ips, port))
                if result == 0:
                    print(f"\033[92m{ips} -> {port} is open!!!\033[00m")
                s.close()
            except:
                pass

if __name__ == "__main__":
    main()