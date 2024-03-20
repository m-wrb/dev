numbers=[1,2,3,4,5]
suqres=[n**2 for n in numbers]
print(suqres)

###
evens=[n for n in numbers if n%2==0]
print(evens)

###
ipList=['192.168.1.1','10.0.0.256','172.16.0.1','256.0.0.1']
validIps=[ip for ip in ipList if all(0<=int(octet)<=255 for octet in ip.split('.'))]
print(validIps)

###
interfaces=[f'GigabitEth0/{i}' for i in range(0,5)]
print(interfaces)

###
subnets=[['192.168.1.1','192.168.1.2'],['10.0.0.1','10.0.0.2']]
allIps=[ip for subnet in subnets for ip in subnet]
print(allIps)