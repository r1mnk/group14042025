import string

in_letters = input("Enter letters in format [a-y] ").strip()

if len(in_letters) == 1:
    result = in_letters
else:
    first_letter, second_letter = in_letters.split("-")
    index_1 = string.ascii_letters.index(first_letter)
    index_2 = string.ascii_letters.index(second_letter)

    start = min(index_1, index_2)
    end = max(index_1, index_2)

    result = string.ascii_letters[start : end + 1]
