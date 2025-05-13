def add_one(some_list: list) -> list:
    num_string = "".join(map(str, some_list))
    summ_int = int(num_string) + 1
    result_str = str(summ_int)
    result_list = list(map(int, str(summ_int)))
    return result_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("ОК")
