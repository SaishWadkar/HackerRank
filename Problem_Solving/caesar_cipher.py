import string
a = list(string.ascii_lowercase)

k = 3

# dict
low_ascii = {}
for i,j in enumerate(string.ascii_lowercase):
    low_ascii[i+1]=j
#print(low_ascii)

# dict
high_ascii = {}
for i,j in enumerate(string.ascii_uppercase):
    high_ascii[i+1]=j
#print(high_ascii)

s = 'xyZ'
cipher =""
for i in s:
    if i.isalpha() and i.islower():
        current = ord(i) # current ascii
        ci = current+k  # new ascii
        if ci>122:
            temp = ci -122
            ci = low_ascii[temp]
            cipher = cipher + ci
        #print(current)
        else:
            cipher=cipher + chr(ci)

    elif i.isalpha() and i.isupper():
        current = ord(i)  # current ascii
        ci = current + k  # new ascii
        if ci > 90:
            temp = ci - 90
            ci = high_ascii[temp]
            cipher = cipher + ci
        # print(current)
        else:
            cipher = cipher + chr(ci)
    else:
        cipher = cipher + i
print(f"Cipher : {cipher}")