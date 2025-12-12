import math

def main():
    with open("input.txt", "r") as file:
        data = file.read()

    lines = data.splitlines()
    points = []
    for line in lines:
        points.append((int(line.split(",")[0]), int(line.split(",")[1])))

    biased_points = []
    min_x = min_y = float("inf")
    max_x = max_y = float("-inf")

    # find the total bounds
    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        if point[0] < min_x:
            min_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
        if point[1] < min_y:
            min_y = point[1]
    
    biased_points = list(map(lambda x: (x[0] - min_x, x[1] - min_y), points))
    print(biased_points)

    # scale
    x_widths = set()
    for i in range(len(points)):
        if i != len(points) - 1:
            if points[i] - points[i+1] != 0:
                x_widths.add(abs(points[i] - points[i+1]))


    # create "image"
    row = "0" * (max_x - min_x) + "\n"
    image = row * (max_y - min_y) 

    print(max_x - min_x)
    print(max_y - min_y)



'''
    dist_map = {}
    for point in points:
        dists = {}
        for i in range(len(points)):
            if points[i] == point:
                continue
            dists[points[i]] = get_area(point, points[i])
        dist_map[point] = dict(sorted(dists.items(), key = lambda x: x[1], reverse = True))

    largest_points = None
    largest_area = float("-inf")
    for key in dist_map:
        largest, *_ = dist_map[key].items()
        if largest[1] > largest_area:
            largest_area = largest[1]
            largest_points = [key, largest[0]]

    print(largest_points)
    print(largest_area)
'''            
    


def get_lowest_common_denominator(*numbers):
    for number in numbers:
            pass

def get_area(p1, p2):
    x = abs(p1[0] - p2[0] + 1)
    y = abs(p1[1] - p2[1] + 1)
    return x * y

def get_distance(p1, p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))

if __name__ == "__main__":
    main()