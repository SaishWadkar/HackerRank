# tin size : 1,3,5,7,10 (L)
size = [10,7,5,3,1]
def no_of_cans(order):
    total = 0
    remainder = None
    while remainder!=0:
        for i in size:
            if order < i:
                continue
            else:
                total += int(order/i)
                remainder = int(order % i)
                order = remainder
    return total
n = 87
print(no_of_cans(n))