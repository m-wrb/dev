numbers=[1,2,3,4,5]
squares={n:n**2 for n in numbers}
print(squares)

###
evenSquares={n:n**2 for n in numbers if n%2==0}
print(evenSquares)

###
devices=['Router1','Switch1','Router2']
ips=['192.168.1.1','192.168.1.2','192.168.1.3']
ipDeviceMap={ips[i]:devices[i] for i in range(len(devices))}
print(ipDeviceMap)

###
interfaces=['Gig0/0','Gig0/1','Fa0/0']
speeds=['1G','1G','100M']
intSpeed={interfaces[i]:speeds[i] for i in range(len(interfaces))}
print(intSpeed)

###
deviceTypes={'Router1':'Router','Switch1':'Switch','Router2':'Router'}
routersOnly={device:type for device, type in deviceTypes.items() if type=='Router'}
print(routersOnly)

###
