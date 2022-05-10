
# Complete the solve function below.
def solve(s):
    text = s.split()
    string = ""
    for i in text:
        i=i.capitalize()
        string = string + i
    return string

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print("Result : ",result)

