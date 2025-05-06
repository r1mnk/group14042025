number = int(input(f"Enter number: "))

while number > 9:
    result = 1
    for int_num in str(number):
        result *= int(int_num)
    number = result
print(number)
