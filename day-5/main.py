def main():
    with open("input.txt", "r") as file:
        data = file.read()

    fresh_ingredients_set = set()
    fresh_ingredients_ranges = []
    
    fresh_ingredients = data.split("\n\n")[0].splitlines()
    available_ingredients = data.split("\n\n")[1].splitlines()
    

    for ingredient_range in fresh_ingredients:

        start, end = ingredient_range.split("-")[0], ingredient_range.split("-")[1]
        fresh_ingredients_ranges.append([int(start), int(end)])
        fresh_ingredients_set.add(range(int(start), int(end) + 1))

    '''
    for i in range(len(fresh_ingredients_ranges)):
        for j in range(len(fresh_ingredients_set)):
            if i != j:
                while fresh_ingredients_ranges[i][0] in fresh_ingredients_set[j]:
                    fresh_ingredients_ranges[i] += 1
                    if fresh_ingredients_ranges[i][0] == fresh_ingredients_ranges[i][1]:
                        fresh_ingredients_ranges.remove(fresh_ingredients_ranges[i])
                        break
                while fresh_ingredients_ranges[i][1] in fresh_ingredients_set[j]:
                    fresh_ingredients_ranges[i] -= 1
    '''

    print(fresh_ingredients_ranges)

    for i in range(len(fresh_ingredients_ranges) - 1):
        for j in range(i+1, len(fresh_ingredients_ranges)):
            print(fresh_ingredients_ranges[i], fresh_ingredients_ranges[j])
            # move i0 out of j
            if (
                fresh_ingredients_ranges[i][0] >= fresh_ingredients_ranges[j][0] 
                and fresh_ingredients_ranges[i][0] <= fresh_ingredients_ranges[j][1]
                ):
                fresh_ingredients_ranges[i][0] = fresh_ingredients_ranges[j][1] + 1
                if fresh_ingredients_ranges[i][0] > fresh_ingredients_ranges[i][1]:
                    fresh_ingredients_ranges[i] = [0, -1]
            # move i1 out of j
            if (
                fresh_ingredients_ranges[i][1] >= fresh_ingredients_ranges[j][0]
                and fresh_ingredients_ranges[i][1] <= fresh_ingredients_ranges[j][1]
                ):
                fresh_ingredients_ranges[i][1] = fresh_ingredients_ranges[j][0] - 1
                if fresh_ingredients_ranges[i][0] > fresh_ingredients_ranges[i][1]:
                    fresh_ingredients_ranges[i] = [0, -1]
            # if j is fully inside i, remove j
            if (
                fresh_ingredients_ranges[i][0] <= fresh_ingredients_ranges[j][0]
                and fresh_ingredients_ranges[i][1] >= fresh_ingredients_ranges[j][1]
                ):
                fresh_ingredients_ranges[j] = [0, -1]
            
        

    count = 0
    for fresh_ingredients_range in fresh_ingredients_ranges:
        count += fresh_ingredients_range[1] - fresh_ingredients_range[0] + 1

    
    print(fresh_ingredients_ranges)
    print(count)

    '''
    for ingredient in available_ingredients:
        for range_set in fresh_ingredients_set:
            if int(ingredient) in range_set:
                count += 1
                break
    '''



    

if __name__ == "__main__":
    main()