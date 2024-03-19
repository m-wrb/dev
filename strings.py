single_quoted_string='Hello, Python!'
double_quoted_string="Hello, Python!"
print(single_quoted_string)
print(double_quoted_string)

###
greeting="Hello"
target="World"
message=greeting+", "+target+"!"
print(message)

###
name="Python"
version=3.8
message=f"Welcome to {name} version {version}!"
print(message)

###
a=5
b=10
result_message=f"The sum of {a} and {b} is {a+b}"
print(result_message)

###
length=len(message)
print(length)

###
cidr_notation='172.168.1.1/24'
ip_address=cidr_notation.split('/')[0]
print(ip_address)

###
first_octet=ip_address[:ip_address.index('.')]
print(first_octet)
second_start=ip_address.index('.')+1
second_end=ip_address.index('.',second_start)
second_ocetet=ip_address[second_start:second_end]
print(second_ocetet)

###
subnet_mask=cidr_notation.split('/')[1]
print(subnet_mask)