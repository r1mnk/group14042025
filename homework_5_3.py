from string import punctuation

raw_input = input("Enter something: ")

clear_string = "".join(char for char in raw_input if char not in punctuation)
words = clear_string.split()
words_capitalized = (word.capitalize() for word in words)
hashtag = "#" + "".join(words_capitalized)
hashtag = hashtag[:140]
