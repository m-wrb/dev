def greet():
    print('Hello Net')

greet()

###
def configInt(intName,ipAdd):
    print(f'Configuring {intName} with IP: {ipAdd}')

configInt('GigabitEth0/1','192.168.1.1')

###
configInt(ipAdd='192.168.1.1', intName='GigEth100/20')

###
def calculateMetrics(bytesTransmitted,bytesReceived):
    txRate=bytesTransmitted/60
    rxRate=bytesReceived/60
    return txRate,rxRate

tx,rx=calculateMetrics(3000,5000)
print(f'Transmit Rate: {tx} Bps, Receive Rate: {rx} Bps')

###
def ping(host='8.8.8.8',count=4):
    print(f'Pinging {host} {count} times...')
    return 'Ping successful'
print(ping())
print(ping('192.168.1.1'))
print(ping(count=8))

###