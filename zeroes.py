def compare_values(number, values) -> str:
    if values[0] > values[1]:
        return f"{number} is zero_special"


def get_zeroes_on_the_right(number):
    numbers = [int(number), int(number) - 1]
    print(numbers)
    return [len(str(x)) - len(str(x).rstrip('0'))
            for x in numbers
            ]


def ask_number():
    value = True
    while value == True:
        number = input("pls, enter a number: ")
        if number.isnumeric():
            value = False
            values = get_zeroes_on_the_right(number)
            print(compare_values(number, values))
        else:
            print(f"the value {number} isn't a number")


if __name__ == "__main__":
    ask_number()
