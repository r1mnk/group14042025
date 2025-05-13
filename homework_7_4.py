def common_elements() -> set:
    set_1 = set()
    set_2 = set()
    for divisible_num in range(100):
        if divisible_num % 3 == 0:
            set_1.add(divisible_num)
        if divisible_num % 5 == 0:
            set_2.add(divisible_num)
    intersection_set = set_1 & set_2
    return intersection_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
