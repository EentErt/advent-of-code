def main():
    with open("input.txt", "r") as file:
        data = file.read()
    
    lines = data.splitlines()

    previous_line = lines[0].replace("S", "1")
    current_line = lines[1]

    print(previous_line)

    paths = 0

    for j in range(1, len(lines)):
        new_line = ""
        for i in range(len(current_line)):
            if current_line[i] == "." and previous_line[i] != "." and previous_line[i] != "^":
                new_line += previous_line[i] + 1
            elif current_line[i] == "^" and previous_line[i] != ".":
                new_line = new_line[0:-1] + "|"
                new_line += "^"
                paths += 1
            elif current_line[i-1] == "^" and previous_line[i-1] == "|":
                new_line += "|"
            else:
                new_line += current_line[i]
        previous_line = new_line
        current_line = lines[j]
        with open("output.txt", "a") as file:
            file.write(new_line + "\n")
        print(new_line, paths)
    print(paths + 1)



if __name__ == "__main__":
    main()