fib_list=[0,1]
for f in range(8):
     g=fib_list[f]+fib_list[f+1]
     fib_list.append(g)

print(fib_list)