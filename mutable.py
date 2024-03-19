my_string="Hello Python!"
try:
    my_string[7]='W'
except TypeError as e:
    print(e)

###

my_list=[1,2,3,4]
my_list[2]=30
print(my_list)

###

original_list=[1,2,3]
new_list=original_list
new_list[1]=200
print(original_list)

###
ind_copy=original_list[:]
ind_copy[1]=20
print(original_list)
print(ind_copy)
print("#### copy ###")
tablica=[3,4,5]
copy_org=tablica.copy()
tablica[1]=16
print(copy_org)
print(tablica)
###
a =10
b=a
b=5
print(a)
print(b)
