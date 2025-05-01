import random

length = random.randint(3, 10)
lst = [random.randint(1, 100) for _ in range(length)]

new_list = [lst[0], lst[2], lst[-2]]
