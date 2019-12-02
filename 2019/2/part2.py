import sys

memory = {1:12, 2:2}

with open(sys.argv[1], "r") as f:
    for line in f:
        ops_original = [int(x) for x in line.strip().split(",")]

for a in range(0,100):
    for b in range(0, 100):
        ops = list(ops_original)
        ops[1] = a
        ops[2] = b

        i = 0
        while True:
            opcode = ops[i]
            if opcode == 1:
                in1, in2, out = ops[i+1:i+4]
                ops[out] = ops[in1] + ops[in2]
                i += 4
            elif opcode == 2:
                in1, in2, out = ops[i+1:i+4]
                ops[out] = ops[in1] * ops[in2]
                i += 4
            elif opcode == 99:
                break

        if ops[0] == 19690720:
            print(a * 100 + b)
            break
