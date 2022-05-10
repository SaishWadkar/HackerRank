x=int(input())
y=int(input())
z=int(input())
n=int(input())

my_list=[]

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                my_list.append((i,j,k))

print(my_list)

