vlans={10,20,30,40,50}
protocols=set(['OSPF','BGP','EIGRP'])
print(vlans)
print(protocols)

###
vlans.add(60)
print(vlans)

###
vlans.remove(10)
protocols.discard('EIGRP')
print(vlans)
print(protocols)

###
print("###")
a={1,2,3}
b={3,4,5}
unionSet=a.union(b)
print(unionSet)

###
intersectionSet=a.intersection(b)
print(intersectionSet)

###
differenceSet=a.difference(b)
print(differenceSet)

###
ips=set()
ips.add('192.168.1.1')
ips.add('10.0.0.1')
ips.add('192.168.1.1')
print(ips)