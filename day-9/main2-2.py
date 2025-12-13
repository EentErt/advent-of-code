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

    searching = True

    largest_points = None
    largest_area = float("-inf")
    while searching:
        largest_area = float("-inf")
        for key in dist_map:
            largest, *_ = dist_map[key].items()
            if largest[1] > largest_area:
                largest_area = largest[1]
                largest_points = [key, largest[0]]

        #check rectangle for collisions:
            #make rectangle
        rectangle = (
            min(largest_points[0][0], largest_points[1][0]), # x1
            min(largest_points[0][1], largest_points[1][1]),
            max(largest_points[0][0], largest_points[1][0]),
            max(largest_points[0][1], largest_points[1][1])
            )
        
            # check for points inside the rectangle
        print("\n\nTrying points:", largest_points)
        print("Area:", largest_area)
        collision = False
        for point in points:
                # x is inside the rectangle 
            if point[0] > rectangle[0] and point[0] < rectangle[2]:
                    # y is inside the rectangle
                if point[1] > rectangle[1] and point[1] > rectangle[3]:
                        # remove the invalid pair from dist_map
                    print(largest_points[0])
                    dist_map[largest_points[0]].pop(largest_points[1])
                    dist_map[largest_points[1]].pop(largest_points[0])
                    print(f"point {point} is inside rectangle {rectangle}")
                    collision = True
                    break 
                continue
        
        if collision is True:
            continue
        # check for line intersections
        for i in range(len(points)):
            start = points[i]
            end = points[0]
            if i != len(points) - 1:
                end = points[i + 1]
            # column
            if end[0] - start[0] == 0:
                if end[0] > rectangle[0] and end[0] < rectangle[2]:
                    # column is inside rectangle bounds
                    if (start[1] <= rectangle[1] and end[1] >= rectangle[3]) or (start[1] >= rectangle[3] and end[1] <= rectangle[1]):
                        dist_map[largest_points[0]].pop(largest_points[1])
                        dist_map[largest_points[1]].pop(largest_points[0])
                        print(f"line {start, end} is through rectangle {rectangle}")
                        collision = True
                        break
                    continue
                continue
            # row
            elif end[1] - start[1] == 0:
                if end[1] > rectangle[1] and end[1] < rectangle[1]:
                    # row is inside rectangle bounds
                    if (start[0] <= rectangle[0] and end[0] > rectangle[2]) or (start[0] > rectangle[2] and end[0] < rectangle[0]):
                        dist_map[largest_points[0]].pop(largest_points[1])
                        dist_map[largest_points[1]].pop(largest_points[0])
                        print(f"line {start, end} is through rectangle {rectangle}")
                        collision = True
                        break
                    continue
                continue


                


        # both checks pass, so no collision found
        if collision is False:
            searching = False


        

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