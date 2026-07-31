'''def requests(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(10)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"\033[92mOpen: {port}\033[00m")
        s.close()
        return result
    except:
        pass'''