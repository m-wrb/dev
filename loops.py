portStatus='up'
if portStatus=='up':
    print('The port is operational')

###
if portStatus=='up':
    print('The port is operational.')
else:
    print("The port is down")

###
portSpeed=100
if portSpeed==100:
    print("Fasteth")
elif portSpeed==1000:
    print('Gigeth')
else:
    print('Speed unrecognized.')

###
intConfig={
    'GigEth0/1':{'status':'up','vlan':'10'},
    'GigEth0/2':{'status':'down','vlan':'20'},
    'GigEth0/3':{'status':'up','vlan':'10'}
}
device={interface:status for interface, status in intConfig.items() if status['vlan']=='20' }
print(device)

###
