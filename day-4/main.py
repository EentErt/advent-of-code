def main():
    data = ""
    with open("input.txt", "r") as file:
        data = file.read()
    lines = data.splitlines()

    count = 0
    available = True
    run = 1
    while available:
        print(f"Run {run}")
        removed = 0
        for i in range(0, len(lines)):
            for j in range(0, len(lines[i])):
                if lines[i][j] == "@":
                    cluster = [
                        "." if i == 0 or j == 0 else lines[i-1][j-1],
                        "." if i == 0 else lines[i-1][j],
                        "." if i == 0 or j == len(lines[i]) - 1 else lines[i-1][j+1],
                        "." if j == 0 else lines[i][j-1],
                        "." if j == len(lines[i]) - 1 else lines[i][j+1],
                        "." if i == len(lines) - 1 or j == 0 else lines[i+1][j-1],
                        "." if i == len(lines) - 1 else lines[i+1][j],
                        "." if i == len(lines) - 1 or j == len(lines[i]) - 1 else lines[i+1][j+1]
                    ]
                    if check_availability(cluster):
                        count += 1
                        removed += 1
                        lines[i] = lines[i][:j] + "x" + lines[i][j+1:]
        
        

        available = any("x" in line for line in lines)
        
        for i in range(len(lines)):
            lines[i] = lines[i].replace("x", ".")
        print(f"{removed} removed")

        run += 1
        
    print(count)

def check_availability(cluster):
    count = 0
    for cell in cluster:
        if cell == "@" or cell == "x":
            count += 1
    return count < 4



if __name__ == "__main__":
    main()