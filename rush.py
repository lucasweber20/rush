import concurrent.futures
import argparse
from scripts.Requests import Requests


parser = argparse.ArgumentParser()

args = parser.add_argument("-ip", "--ip", help='Set ip, example: -ip 192.168.0.100', type=str)
args = parser.add_argument("-l", "--list", help="Specify list ip, example: -l ips.txt", type=str)
args = parser.add_argument("-p", "--port", help="Specify port to scan, example: -p 22, 1-100 or 80,443", type=str)

args = parser.parse_args()

def main():
    # Flags
    host = args.ip
    port = args.port
    list = args.list

    # Requests
    req = Requests(host, port)
    req.requests()

if __name__ == "__main__":
    main()