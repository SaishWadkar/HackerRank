'''
 :keyword ord : returns ascii value of character
          chr : returns character value of ascii
'''

import string

s= 'XYZ'
k = 3
cipher = ''
for i in s:
    if i.islower():
        num=((ord(i)-97+k)%26)
        #print(num)
        cipher+=chr(num+97)
    elif i.isupper():
        num = ((ord(i) - 65 + k) % 26)
        #rint(num)
        cipher += chr(num + 65)
    else:
        cipher+=i
print(cipher)


