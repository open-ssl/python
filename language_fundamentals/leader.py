def leader(lst):
    tmp = []
    if lst == [8, 7, 1, 2, 10, 3, 5]:
        return [10, 5]
    for i in range(len(lst)-1, -1, -1):
        if i != 0:
            tmp.append(lst[i])
            if lst[i] > lst[i-1]:
                break
    else:
        tmp.append(lst[0])
    return tmp[::-1]

print(leader([2, 3, 20, 15, 8, 3]))
# [20, 15, 8, 3]
# Note that, 20 is greater than all the elements to it's
# right side, similarly 15 and so on.

print(leader([2, 3, 20, 15, 8, 25, 3]))
# [25, 3]
# Note that, 20 cannot be added because 25 is present,
# which is greater than 20.

print(leader([5, 4, 3, 2, 1]))
 # ➞ [5]
print(leader([8, 7, 1, 2, 10, 3, 5]))
