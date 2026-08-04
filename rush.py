import concurrent.futures
import argparse
from scripts.Requests import Requests
from scripts.Parser import Parser


parser = argparse.ArgumentParser()

args = parser.add_argument("-ip", "--ip", help='Set ip, example: -ip 192.168.0.100', type=str)
args = parser.add_argument("-p", "--port", help="Specify port to scan, example: -p 22, 1-100 or 80,443", type=str)
args = parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 5", default=1, type=int)
args = parser.add_argument("-si", help="Search for hosts, example: -si", action='store_true')

args = parser.parse_args()

def main():
    # Flags
    host = args.ip
    port = args.port
    thread = args.thread
    scan_hosts = args.si

    # Parser
    ports = Parser(port)
    ports_list = ports.parser()
    
    # Requests
    req = Requests()
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as executor:
        futures = [executor.submit(req.requests, host, port) for port in ports_list]
        print(f"===== \033[92m{host}\033[00m =====")
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result[0] == 0:
                print(f"\033[92mOpen: {result[1]}\033[00m")

if __name__ == "__main__":
    main()