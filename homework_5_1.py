import keyword
import string

variable = input(f"Enter variable: ")
error_msg = f"Wrong input. Validate your variable {variable}"
bad_symbol = string.punctuation.replace("_", "")

if variable[0].isdigit():
    print(False)
elif set(variable) == {"_"} and variable.count("_") > 1:
    print(False)
elif variable in keyword.kwlist:
    print(False)
elif any(char.isupper() for char in variable):
    print(False)
elif any(char in bad_symbol or char.isspace() for char in variable):
    print(False)
else:
    print(True)
