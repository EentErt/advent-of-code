def main():
    data = ""
    with open("input.txt", "r") as file:
        data = file.read()
    entries = data.split(",")
    invalid_sum = 0
    for entry in entries:
        entry_range = (int(entry.split("-")[0]), int(entry.split("-")[1]))
        for i in range(entry_range[0], entry_range[1] + 1):
            if not check_repeats(i):
                invalid_sum += i
    print(invalid_sum)



def is_valid(num):
    num_str = str(num)
    if len(num_str) % 2 != 0:
        return True
    if num_str[0:len(num_str)//2] == num_str[len(num_str)//2:]:
        return False
    return True


def check_repeats(num):
    num_str = str(num)
    for i in range(1, len(num_str) // 2 + 1):
        if len(num_str) % i != 0:
            continue
        
        # break num_str into chunks of length i
        chunks = [num_str[j:j+i] for j in range(0, len(num_str), i)]
        if all(chunk == chunks[0] for chunk in chunks):
            return False
    return True


if __name__ == "__main__":
    main()