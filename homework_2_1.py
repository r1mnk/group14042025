input_number = int(input(f"Enter your number: "))

first_num, first_dig = divmod(input_number, 10)
second_num, second_dig = divmod(first_num, 10)
third_num, third_dig = divmod(second_num, 10)
fourth_num, fourth_dig = divmod(third_num, 10)

print(fourth_dig)
print(third_dig)
print(second_dig)
print(first_dig)
