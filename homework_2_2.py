input_number = int(input(f"Enter your number: "))

first_num, first_dig = divmod(input_number, 10)
second_num, second_dig = divmod(first_num, 10)
third_num, third_dig = divmod(second_num, 10)
fourth_num, fourth_dig = divmod(third_num, 10)
fifth_num, fifth_dig = divmod(fourth_num, 10)

print(f"{first_dig}{second_dig}{third_dig}{fourth_dig}{fifth_dig}")
