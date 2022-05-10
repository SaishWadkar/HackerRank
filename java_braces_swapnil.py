from collections import deque
from collections import Counter
from stack import MyStack

# stack = deque()
# chars = Counter(line)

# multi line i/p from user
print("Enter/Paste your code. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError as e:
        # print(f"{e}")
        break
    contents.append(line)

print(contents)

# 1 using list as stack
list1 = []

# 2 using user definde stack class
s = MyStack()
# s.push("{")
# s.push("{")
#
# s.pop()
#
# print(s.is_empty())

for line in contents:
    print(f"Line : {line}")

    if "{" in line:
        no = line.count("{")
        print(no)
        for _ in range(no):
            #list1.append("{")
            s.push("{")

    if "}" in line:
        if s.is_empty():
            print("ERROR- already empty")
            break
        else:
            no = line.count("}")
            print(no)
            if no>s.lenght():
                print("ERROR - mismatch")
                break
            else:
                # pop
                for _ in range(no):
                    s.pop()

else:
    print("Success")

# if s.is_empty():
#     print("Success")
# else:
#     print("Fail")


# using counter
# result = Counter(contents[0])
# print(result)
# for i in result.items():
#     print(f"{i}")
#     #print(f"{i[0]} and {i[1]}")









