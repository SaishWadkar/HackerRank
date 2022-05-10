
temp=list(map(int , input().split()))
n=temp[0]
m=temp[1]
happiness=0
my_list=list(map(int , input().split()))
A = set(map(int , input().split()))
B = set(map(int , input().split()))

for i in my_list:
    if i in A:
        happiness=happiness+1
    elif i in B:
        happiness = happiness - 1

print(happiness)