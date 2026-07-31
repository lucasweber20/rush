import socket


class Requests:
    def __init__(self):
        pass

    def requests(self, host, port):
        port = int(port[0])
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(10)
            result = s.connect_ex((host, port))
            s.close()
            return result
        except:
            pass