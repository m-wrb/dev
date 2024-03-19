my_list = [1,2,3,"Python",3.14]
print(my_list)

for item in my_list:
    print(item)

for index, item in enumerate(my_list):
    print(index,item)

squared_numbers = [x**2 for x in range(10)]
print("#####################3")
print(squared_numbers)