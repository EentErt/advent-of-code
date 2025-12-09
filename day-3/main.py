def main():
    data = ""
    with open("input.txt", "r") as file:
        data = file.read()

    lines = data.splitlines()
    highest, remainder = 0, ""
    total = 0
    for line in lines:
        print(line)
        highest = get_highest_twelve(line)
        print(highest, remainder)
        total += highest
    print(total)

def get_highest_twelve(line):
    highest, remainder, last_index = "", line, -1
    for i in range(12):
        print(f"\033[31m{line[:last_index+1]}\033[0m{line[last_index+1:len(line)-11+i]}\033[31m{line[len(line)-11+i:]}\033[0m")
        digit, index = find_highest(line[last_index+1:len(line)-11+i])
        highest += digit
        last_index += index + 1
        remainder = remainder[last_index + 1:]
    return int(highest)

def get_highest(line):
    tens, remainder = find_highest(line[:-1:])
    remainder = remainder + line[-1]
    print(tens * 10, remainder)
    ones, remainder = find_highest(remainder)
    print(ones, " " + remainder)
    result = tens * 10 + ones
    return result, remainder

def find_highest(chars):
    highest = "0"
    to_remove = 999
    for i in range(len(chars)):
        if int(chars[i]) > int(highest):
            highest = chars[i]
            to_remove = i
    return highest, to_remove

if __name__ == "__main__":
    main()