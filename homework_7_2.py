def correct_sentence(text: str) -> str:
    result = text[0].upper() + text[1:]
    if not text.endswith("."):
        result += "."
    return result


assert correct_sentence("greetings, friends") == "Greetings, friends.", "Test1"
assert correct_sentence("hello") == "Hello.", "Test2"
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", "Test3"
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", "Test4"
assert correct_sentence("greetings, friends.") == "Greetings, friends.", "Test5"
print("ОК")
