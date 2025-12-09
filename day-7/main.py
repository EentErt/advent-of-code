import math

def main():
    with open("input.txt", "r") as file:
        data = file.read()
    
    lines = data.splitlines()

    previous_line = lines[0].replace("S", "|")
    current_line = lines[1]

    splits = 0
    paths = 1
    branches = [1]
    paths_list = []
    path_list = []
    for j in range(len(lines[0])):
        if lines[0][j] == "S":
            path_list.append(1)
        else:
            path_list.append(0)
    paths_list.append(path_list)
        


    for j in range(1, len(lines)):
        new_line = ""
        branch = 0
        for i in range(len(current_line)):
            if current_line[i] == "." and previous_line[i] == "|":
                new_line += "|"
                if new_line[i-1] == "^":
                    paths += 1
            elif current_line[i] == "^" and previous_line[i] == "|":
                # joining an existing path
                if new_line[i-1] == "|":
                    paths += 1
                new_line = new_line[0:-1] + "|"
                new_line += "^"
                splits += 1
                branch += 1
            elif current_line[i-1] == "^" and previous_line[i-1] == "|":
                new_line += "|"
                paths += 1
            else:
                new_line += current_line[i]

        paths_to = []
        for i in range(len(new_line)):
            path_to = paths_list[j-1][i]
            if new_line[i] == "^":
                path_to = 0
            if new_line[i] == "|":
                if i < len(new_line) - 1 and new_line[i+1] == "^":
                    path_to += paths_list[j-1][i+1]
                if new_line[i-1] == "^":
                    path_to += paths_list[j-1][i-1]
            paths_to.append(path_to)
        paths_list.append(paths_to)

        path_count = 0
        for path in paths_list[j]:
            path_count += path



        branches.append(branches[j-1] + branch)
        previous_line = new_line
        current_line = lines[j]
        print(new_line, paths, splits, path_count)
    print(paths)


if __name__ == "__main__":
    main()