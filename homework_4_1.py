lst_first = [0, 1, 0, 12, 3]
lst_second = [1, 0, 13, 0, 0, 0, 5]
lst_third = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

lst_zero = []
lst_non_zero = []

for num in lst_third:
    if num == 0:
        lst_zero.append(num)
        # print(lst_zero)
    else:
        lst_non_zero.append(num)

result = lst_non_zero + lst_zero

print(result)
