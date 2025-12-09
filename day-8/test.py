def main():
    first_set = {(1, 2, 3), (4, 5, 6), (7, 8, 9)}
    second_set = [(1, 2, 3), (6, 7, 8)]
    if second_set[0] in first_set:
        print("yes")

main()