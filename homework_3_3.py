lst = [1, 2, 3, 4, 5, 6, 7]

full_list = len(lst)

if full_list % 2 == 0:
    half_list = len(lst) // 2
    half_list_result = lst[:half_list], lst[half_list:]
    print(half_list_result)
else:
    half_list = (len(lst) + 1) // 2
    half_list_result = [lst[:half_list], lst[half_list:]]
    print(half_list_result)
