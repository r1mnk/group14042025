lst = [3, 8, 15, 20, 21]

if len(lst) == 1:
    print(f"Nothing to do: {lst}")
elif len(lst) == 0:
    print(f"List is empty")
else:
    last_num = lst.pop()
    lst.insert(0, last_num)
    print(lst)
