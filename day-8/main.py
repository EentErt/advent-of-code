import math

def main():
    with open("input.txt", "r") as file:
        data = file.read()
    
    lines = data.splitlines()
    boxes = []
    unconnected = set()
    connections = 0
    circuits = []

    for line in lines:
        coords = line.split(",")
        boxes.append((int(coords[0]), int(coords[1]), int(coords[2])))

    dist_map = {}

    shortest_distance = float("inf")
    next_pair = None

    # initialize
    for i in range(len(boxes)):
        unconnected.add(boxes[i])
        distances = {}
        for j in range(len(boxes)):
            if i == j:
                continue
            dist = get_distance(boxes[i], boxes[j])
            if boxes[j] not in distances:
                distances[boxes[j]] = dist
        dist_map[boxes[i]] = dict(sorted(distances.items(), key = lambda x: x[1]))

    # make first 1000 connections
    connecting = True
    while connecting:
        # connect closest pair
        shortest_distance = float("inf")
        for key in dist_map:
            dest = None      
            if len(dist_map[key]) > 0:
                dest, *_ = dist_map[key].items()
            else: 
                continue
            if dest[1] < shortest_distance:
                shortest_distance = dest[1]
                next_pair = [key, dest[0]]
        connections += 1

        dist_map[next_pair[0]].pop(next_pair[1])
        dist_map[next_pair[1]].pop(next_pair[0])

        

        # make circuit
        connect_circuits = set()
        connect_circuits.update(next_pair)
        for circuit in circuits:
            if next_pair[0] in circuit and next_pair[1] in circuit:
                connect_circuits = set()
                # connections -= 1
                break
            elif next_pair[0] in circuit or next_pair[1] in circuit:
                connect_circuits.update(circuit)
                circuits.remove(circuit)
        if len(connect_circuits) > 0:
            circuits.append(connect_circuits)

        print(connections, shortest_distance)

        if connections == 1000:
            connecting = False

    longest_three = sorted(circuits, key = lambda x: len(x), reverse = True)[0:3]
    result = 1
    for circuit in longest_three:
        print(circuit)
        print(len(circuit))
        result *= len(circuit)
                
    print(result)









def get_distance(box1, box2):
    return math.sqrt(math.pow(box1[0] - box2[0], 2) + math.pow(box1[1] - box2[1], 2) + math.pow(box1[2] - box2[2], 2))

if __name__ == "__main__":
    main()