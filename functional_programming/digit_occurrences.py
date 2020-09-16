def digit_occurrences(n1, n2, src_num):
    return sum([str(i).count(str(src_num)) for i in range(n1, n2+1)])

# print(digit_occurrences(51, 55, 5))
# 6
# [51, 52, 53, 54, 55] : 5 occurs 6 times

# digit_occurrences(1, 8, 9)  0

# print(digit_occurrences(-8, -1, 8))
  # 1

# digit_occurrences(71, 77, 2)  1
