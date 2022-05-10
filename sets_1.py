n = int(input())
s = set(map(int, input().split()))
N = int(input())
commands = []
for i in range(N):
    cmd = input().split()

    if len(cmd) == 2:
        tup = (cmd[0], int(cmd[1]))
        commands.append(tup)
    else:
        tup = (cmd[0], -1)
        commands.append(tup)

# execute commands
print(s)
print(commands)
for tup in commands:
    cmd, no = tup
    if cmd == "pop" and no == -1:
        print("Popped : ", s.pop())
    elif cmd == "remove":
        if no in s:
            s.remove(no)
            print("Removed : ", no)
    elif cmd == "discard":
        s.discard(no)
        print("Discarded : ", no)

print(s)
print(sum(s))

# print(commands)
