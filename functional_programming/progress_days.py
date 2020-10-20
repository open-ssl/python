def progress_days(lst):
    return len([i for i in range(1, len(lst)) if lst[i-1] < lst[i]])

print(progress_days([3, 4, 1, 2]))
 # ➞ 2
# # There are two progress days, (3->4) and (1->2)
#
print(progress_days([10, 11, 12, 9, 10]))
 # ➞ 3
#
# progress_days([6, 5, 4, 3, 2, 9]) ➞ 1
#
# progress_days([9, 9])  ➞ 0
