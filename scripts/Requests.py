import socket
import re


class Requests:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def requests(self):
        port = int(self.port)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(10)
            result = s.connect_ex((self.host, port))
            if result == 0:
                print(f"\033[92mOpen: {self.port}\033[00m")
            s.close()
            return result
        except:
            pass