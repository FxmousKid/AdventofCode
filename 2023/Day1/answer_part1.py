from io import TextIOWrapper
import sys

def get_first_digit(line: str) -> str :
    num_txt = [str(i) for i in range(10)]

    first_digit: str = ""
    for char in line :
        if char in num_txt :
            first_digit = char
            break

    return first_digit


def get_calibation(line: str) -> int :
    first_digit: str = get_first_digit(line)
    last_digit: str = get_first_digit(line[::-1])
   
    if first_digit + last_digit == "" :
        return 0

    return (int(first_digit + last_digit))

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
