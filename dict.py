device={
    'hostname':'Router1',
    'ip':'192.168.1.1',
    'model':'Cisco 2901',
    'interfaces':['Gigabit0','Gigabit1']
}
print(device)

###
ipAddress=device['ip']
print(f'Device IP Address: {ipAddress}')

###
device['location']='DC A'
print(device)

###
device['ip']='8.8.8.8'
print(device)

###
del device['model']
location=device.pop('location')
print(f'DELETED: {location}')
print(device)

###
for key in device.keys():
    print(key)

###
for value in device.values():
    print(value)

###
for key,value in device.items():
    print(f'{key}:{value}')

###
routingTable={
    '10.0.0.0/24':'192.168.1.1',
    '172.16.0.0/16':'192.168.2.1'
}
for network,nextHop in routingTable.items():
    print(f'Dest: {network}, Next-hop: {nextHop}')