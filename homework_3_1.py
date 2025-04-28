from pywebio.input import FLOAT, NUMBER
from pywebio.output import put_html, put_success, put_error
from pywebio.input import input as pw_input

put_html("<h1>Welcome to the calculator</h1>")

first_num = pw_input("Enter first number", type=NUMBER, required=True)
second_num = pw_input("Enter second number", type=NUMBER, required=True)
operation = pw_input("Enter operation (+, -, *, /):", required=True)

if operation == "/":
    if second_num == 0:
        put_error(f"Cannot divide by zero")
        exit(1)
    result = first_num / second_num
elif operation == "+":
    result = first_num + second_num
elif operation == "-":
    result = first_num - second_num
elif operation == "*":
    result = first_num * second_num
else:
    put_error("Invalid input")
    exit(1)

put_success(f"Your result is: {result}")
