def fun(s):
    # return True if s is a valid email, else return False
    s.strip()
    if (' ' in s) or ('@' not in s) or ('.' not in s):
        return False
    if s.count('@')>1:
        return False
    if s.count('.')>1:
        return False
    if s.index('@') > s.index('.'):
        return False

    split_list_at_the_rate = s.split("@")
    split_list_dot = split_list_at_the_rate[1].split(".")

    print("Splitted list @ left : ",split_list_at_the_rate[0])
    print("Splitted list @ right : ", split_list_at_the_rate[1])
    print()
    print("Splitted list . left : ", split_list_dot[0])
    print("Splitted list . right : ", split_list_dot[1])

    flag = 0
    # 1 username check
    if split_list_at_the_rate[0].isalnum() or '-' in split_list_at_the_rate[0] or '_' in split_list_at_the_rate[0]:
        # 2 website name check
        if split_list_dot[0].isalnum():
            # 3 extension check
            if len(split_list_dot[1])<=3:
                return True

    return False


###########################################################

def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)