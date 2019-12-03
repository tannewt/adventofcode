import sys

wires = []
all_steps = []

with open(sys.argv[1], "r") as f:
    for line in f:
        ops = [x for x in line.strip().split(",")]
        x = 0
        y = 0
        locations = set()
        wires.append(locations)

        steps = {}
        all_steps.append(steps)
        step_count = 1

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
                location = (x, y)
                locations.add(location)
                if location not in steps:
                    steps[location] = step_count
                step_count += 1

        print()

crosses = wires[0] & wires[1]

closest = None
for cross in crosses:
    distance = all_steps[0][cross] + all_steps[1][cross]
    if not closest or distance < closest:
        closest = distance

print(closest)