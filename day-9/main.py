import math

def main():
    with open("input.txt", "r") as file:
        data = file.read()

    lines = data.splitlines()
    points = []
    for line in lines:
        points.append((int(line.split(",")[0]), int(line.split(",")[1])))

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
            
    




def get_area(p1, p2):
    x = abs(p1[0] - p2[0] + 1)
    y = abs(p1[1] - p2[1] + 1)
    return x * y

def get_distance(p1, p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))

if __name__ == "__main__":
    main()