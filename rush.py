import argparse


parser = argparse.ArgumentParser()

args = parser.add_argument("-ip", "--ip", help='Set ip, example: -ip 192.168.0.100', type=str)
args = parser.add_argument("-l", "--list", help="Specify list ip, example: -l ips.txt", type=str)
args = parser.add_argument("-p", "--port", help="Specify port to scan, example: -p 22", type=str)
args = parser.add_argument("-o", "--output", help="Specify output file, example: -o outputs.txt", type=str)
args = parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 2", type=int)

args = parser.parse_args()

def main():
    pass

if __name__ == "__main__":
    main()