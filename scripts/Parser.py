

class Parser:
    def __init__(self, port):
        self.port = port

    def parser(self):
        ports_parsed = []
        if "," in self.port:
            for port in self.port.split(","):
                ports_parsed.append(port)
        elif "-" in self.port:
            for port in self.port.split('-'):
                ports_parsed.append(port)
        else:
            ports_parsed.append(self.port)
        return ports_parsed