def main():
    with open("input.txt", "r") as file:
        data = file.read()
    
    lines = data.splitlines()
    clean_lines = []
    j = 0
    for i in range(len(lines[0])):
        if all(line[i] == " " for line in lines):
            numbers = []
            for line in lines:
                numbers.append(line[j:i])
            j = i + 1
            clean_lines.append(numbers)
        elif i == len(lines[0]) - 1:
            numbers = []
            for line in lines:
                numbers.append(line[j:i+1])
            clean_lines.append(numbers)
        i += 1

    results = 0
    
    for i in range(len(clean_lines)):
        operator = clean_lines[i][-1].strip()
        operands = clean_lines[i][:-1]
        operands = transpose(*operands)
        result = do_math(operator, *operands)
        results += result
        print(result)
    print("Final Result:", results)

def transpose(*numbers):
    result = []
    i = 0
    while True:
        new_number = ""
        for number in numbers:
            if i < len(number):
                new_number += number[i]
        result.append(int(new_number.strip()))
        i += 1
        if all(i >= len(number) for number in numbers):
            break
    return result


def do_math(operator, *args):
    match operator:
        case "*":
            multiple = 1
            for arg in args:
                multiple *= int(arg)
            return multiple
        case "+":
            sum = 0
            for arg in args:
                sum += int(arg)
            return sum
        case _:
            raise ValueError("Unknown Operator:", operator)


if __name__ == "__main__":
    main()