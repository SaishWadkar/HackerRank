
M = int(input())
a=set(map(int , input().split()))

N = int(input())
b=set(map(int , input().split()))

if len(a)!=M and len(b)!=N:
    print("Length exceeded !")
else:
    result=list(a.difference(b))
    result.sort()

    print(result)
