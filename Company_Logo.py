
s = input()
a = []
dict = {}

for i in s:
    a.append(i)
    dict[i]=s.count(i)

# sort alphabetically
a.sort()

#print("Dictionary")

# To print dictionary

# for i,j in dict.items():
#     print("Key ",i)
#     print("Value ",j)
#     print()

for i in a:
