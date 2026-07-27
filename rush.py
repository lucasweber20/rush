import socket
import argparse
import sys


parser = argparse.ArgumentParser()

args = parser.add_argument("-ip", "--ip", help='Set ip, example: -ip 192.168.0.100', type=str)
args = parser.add_argument("-l", "--list", help="Specify list ip, example: -l ips.txt", type=str)
args = parser.add_argument("-p", "--port", help="Specify port to scan, example: -p 22", type=int)
args = parser.add_argument("-o", "--output", help="Specify output file, example: -o outputs.txt", type=str)
args = parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 2", type=int)

args = parser.parse_args()

def main():
    if args.ip:
        result = scan(args.ip)
    elif args.list:
        result = scan(args.list)

def scan(ip):
    if args.ip:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(5)
            result = s.connect_ex((args.ip, args.port))
            if result == 0:
                print(f"{args.port} is open!!!")
            s.close()
        except KeyboardInterrupt:
            print("Exiting programa!")
            sys.exit()
        except socket.error:
            print("Server not responding!")
            sys.exit()
    elif args.list:
        pass

if __name__ == "__main__":
    main()