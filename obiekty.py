##88-91
class NetworkDevice:
    def __init__(self,hostname,ipAddress):
        self.hostname=hostname
        self.ipAddress=ipAddress

###
router=NetworkDevice("Router",'192.168.1.1')
print(f'Device: {router.hostname}, IP: {router.ipAddress}')

###
class NetworkDevice:
    def __init__(self,hostname,ipAddress):
        self.hostname=hostname
        self.ipAddress=ipAddress
    
    def displayConfig(self):
        print(f'Hostname: {self.hostname}, IP: {self.ipAddress}')

router=NetworkDevice("Router",'192.168.1.1')
router.displayConfig()

###