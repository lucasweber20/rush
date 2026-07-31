import concurrent.futures
import argparse
import time
from scripts.Requests import Requests


parser = argparse.ArgumentParser()

args = parser.add_argument("-ip", "--ip", help='Set ip, example: -ip 192.168.0.100', type=str)
args = parser.add_argument("-p", "--port", help="Specify port to scan, example: -p 22, 1-100 or 80,443", nargs="+", type=str)
args = parser.add_argument("-l", "--list", help="Specify list ip, example: -l ips.txt", type=str)
args = parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 5", default=1, type=int)

args = parser.parse_args()

def main():
    # Flags
    host = args.ip
    port = args.port
    thread = args.thread
    
    # Requests
    req = Requests()
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as executor:
        futures = [executor.submit(req.requests, host, port) for p in port]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result == 0:
                print(f"\033[92mOpen: {port[0]}\033[00m")

if __name__ == "__main__":
    main()