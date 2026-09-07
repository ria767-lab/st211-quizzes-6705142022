import re

def convert(number: str) -> int:

    # Check that the input is a string and is not empty
    if not isinstance(number, str) or number == "":
        raise ValueError("Invalid Roman numeral")

    # ONLY valid Roman numeral formats are allowed
    pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

    if not re.fullmatch(pattern, number):
        raise ValueError("Invalid Roman numeral")

    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0

    for i in range(len(number)):
        if i + 1 < len(number) and values[number[i]] < values[number[i + 1]]:
            total -= values[number[i]]
        else:
            total += values[number[i]]

    return total