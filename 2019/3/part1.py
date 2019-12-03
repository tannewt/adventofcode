import sys

wires = []

with open(sys.argv[1], "r") as f:
    for line in f:
        ops = [x for x in line.strip().split(",")]
        x = 0
        y = 0
        locations = set()
        wires.append(locations)

        for op in ops:
            print(op)
            direction = op[0]
            distance = int(op[1:])
            for i in range(distance):
                if direction == "R":
                    x += 1
                elif direction == "L":
                    x -= 1
                elif direction == "U":
                    y -= 1
                elif direction == "D":
                    y += 1
                locations.add((x, y))
        print()

crosses = wires[0] & wires[1]

closest = None
for cross in crosses:
    distance = abs(cross[0]) + abs(cross[1])
    if not closest or distance < closest:
        closest = distance

print(closest)