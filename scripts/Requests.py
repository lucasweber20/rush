import socket
import subprocess


class Requests:
    def __init__(self):
        pass

    def requests(self, host, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(3)
            result = s.connect_ex((host, int(port)))
            s.close()
            return result, port
        except:
            pass

    def scan_hosts(self):
        active_hosts = []
        for num in range(0, 256):
            ip = f"192.168.0.{num}"
            res = subprocess.run(["ping", ip, "-n", "1"], capture_output=True, text=True)
            if "TTL" in res.stdout:
                active_hosts.append(ip)
        return active_hosts
            