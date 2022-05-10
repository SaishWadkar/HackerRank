from collections import Counter

a = [1,1,1,2,2,3,4,5,6,3,4,5,6,7,8,9]
obj = Counter(a)
data=dict(obj)
#print(obj.items())

data[1]=100
data.update({1000:500})
print(data)