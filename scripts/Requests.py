import socket


class Requests:
    def __init__(self):
        pass

    def requests(self, host, port):
        try:
            print(port)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(3)
            result = s.connect_ex((host, int(port)))
            s.close()
            return result, port
        except:
            pass