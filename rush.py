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
    pass

if __name__ == "__main__":
    main()