def generate_cube_numbers(end):
    for num in range(2, end):
        result = num**3
        if result > end:
            return
        yield result


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, "Test0"
assert list(generate_cube_numbers(10)) == [8]
assert list(generate_cube_numbers(100)) == [8, 27, 64]
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
