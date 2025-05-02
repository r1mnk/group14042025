answer = "yes"

while answer in ["yes", "y"]:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /):")
    if operation == "/":
        if second_num == 0:
            print(f"Cannot divide by zero")
            exit(1)
        result = first_num / second_num
    elif operation == "+":
        result = first_num + second_num
    elif operation == "-":
        result = first_num - second_num
    elif operation == "*":
        result = first_num * second_num
    else:
        print("Invalid input")
        exit(1)
    print(result)
    answer = input("Continue?")
