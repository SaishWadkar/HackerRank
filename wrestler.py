def max_weight(players):
    total = len(players)
    if total % 2==0:
        print(f"Total Players : {total}")
        groups = []
        # check for even numbers
        j = int(total/2)
        limit = int(len(players)/2)
        #print(f"j : {j}")
        #print()
        for i in range(limit):
            #print(f"i : {i}")
            #print(f"j : {j}")
            groups.append((players[i],players[j]))
            j+=1
            #print()
        print("Group of players : ")
        print(groups)
        # calculate sum
        max = 0
        for i in groups:
            temp = sum(i)
            if temp>max:
                max = temp

        return max
    else:
        return 0

players = [61,92,82,93,69,88,99,83,67,77,82,89]
print("Maximum weight group : ")
print(max_weight(players))

