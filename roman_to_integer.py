def roman_to_integer(roman):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    for i in range(len(roman)):
        value = roman_dict[roman[i]]

        if i + 1 < len(roman) and roman_dict[roman[i + 1]] > value:
            total -= value

        else:
            total += value

    return total

if __name__ == '__main__':
    roman = input("Enter a roman number for convert to integer: ")

    convert_roman = roman_to_integer(roman)
    print(convert_roman)