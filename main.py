import os

def main():
    data = []
    with open("day1_input.txt", "r") as file:
        data = file.read().splitlines()

    count = 0

    pointer = 50    # [start, end]
    for entry in data:
        if entry.startswith("R"):
            num = int(entry.lstrip("R"))
            for i in range(num):
                pointer = (pointer + 1) % 100
                if pointer == 0:
                    count += 1
        elif entry.startswith("L"):
            num = int(entry.lstrip("L"))
            for i in range(num):
                pointer = (pointer - 1) % 100
                if pointer == 0:
                    count += 1


    print(count)





if __name__ == "__main__":
    main()
