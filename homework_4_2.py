lst = [0, 1, 7, 2, 4, 8]
num_result = []

if lst:
    for inx, num in enumerate(lst):
        if inx % 2 == 0:
            num_result.append(num)
    final = sum(num_result) * lst[-1]
else:
    final = 0

print(final)
