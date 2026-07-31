

class Parser:
    def __init__(self, port):
        self.port = port

    def parser(self):
        ports_parsed = []
        if "," in self.port:
            for port in self.port.split(","):
                ports_parsed.append(port)
        elif "-" in self.port:
            list_range = []
            for port in self.port.split('-'):
                list_range.append(int(port))
            ports_parsed = list(range(list_range[0], list_range[1]+1))
        else:
            ports_parsed.append(self.port)
        return ports_parsed