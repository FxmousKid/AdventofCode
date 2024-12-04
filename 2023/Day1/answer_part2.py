from io import TextIOWrapper
import sys

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits_rev = [digit[::-1] for digit in digits]
digits_rev = digits
num_txt = [str(i) for i in range(1, 10)]


def check_if_number(trimmed_line: str, digits: list[str]) -> str :
    for digit in digits :
        if digit == trimmed_line[:len(digit)] :
            return digit

    for num in num_txt :
        if num == trimmed_line[0] :
            return num
    
    return ""

def get_first_digit(line: str, digits: list[str]) -> str :
    first_digit: str = ""
    
    for _ in line :
        first_digit = check_if_number(line, digits)
        if first_digit != "" :
            return first_digit
        line = line[1:]
        
    return first_digit


def get_calibation(line: str) -> int :
    first_digit = get_first_digit(line, digits)
    last_digit = get_first_digit(line.strip(first_digit), digits_rev)

    f = 0
    if first_digit in digits :
        f = digits.index(first_digit) + 1
    elif first_digit in digits_rev :
        f = digits_rev.index(first_digit) + 1
    elif first_digit in num_txt:
        f = num_txt.index(first_digit) + 1

    l = 0
    if last_digit in digits :
        l = digits.index(last_digit) + 1
    elif last_digit in  digits_rev:
        l = digits_rev.index(last_digit) + 1
    elif last_digit in num_txt :
        l = num_txt.index(last_digit) + 1
    
    print(f"line = {line}, First digit = {first_digit}, Last digit = {last_digit}, f = {f}, l = {l}")
    
    if first_digit == "" :
        return 0
    if last_digit == "" :
        return int(str(f) + str(f))

    return (int(str(f) + str(l)))

def calculate_all_calibration_values(input_file: TextIOWrapper) -> int :
    tmp: str = input_file.read()
    data: list[str] = tmp.split("\n")

    result: int = sum([get_calibation(line) for line in data])
    return result

def main() -> None :
    if (len(sys.argv) != 2) :
        print("Wrong number of arguments");
        print(f"Usage: python3 {sys.argv[0]} <input_file>");
        return None
    with open(sys.argv[1], "r") as input_file :
        result: int = calculate_all_calibration_values(input_file)
        print(f"Sum of all calibration values = {result}")

main()
