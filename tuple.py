device=('Router','192.168.1.1','cisco')
print(device)

###
interface='Gig0', 'up'
print(interface)

###
try:
    device[1]='192.168.2.1'
except TypeError as e:
    print(e)

###
name,ip,brand=device
print(f'Name: {name}, IP: {ip}, Brand: {brand}')

###
dviceInfo=('Router1','172.6.01.1','Juniper',22)
endPoint=('10.10.10.1',443)
