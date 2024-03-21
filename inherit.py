class NetworkDevice:
    def __init__(self,hostname,ipAddress):
        self.hostname=hostname
        self.ipAddress=ipAddress
    
    def displayConfig(self):
        print(f'Hostname: {self.hostname}, IP: {self.ipAddress}')

class Router(NetworkDevice):
    def __init__(self,hostname,ipAddr,routingProtocol):
        super().__init__(hostname,ipAddr)
        self.routingProtocol=routingProtocol

    ###POLY
    def displayConfig(self):
        super().displayConfig()
        print(f'Routing Protocol: {self.routingProtocol}')

router = Router("Router1",'192.168.1.1','OSPF')
#print(f'Routing Protocol: {router.routingProtocol}')
router.displayConfig()

