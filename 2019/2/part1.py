import sys

with open(sys.argv[1], "r") as f:
    for line in f:
        ops = [int(x) for x in line.strip().split(",")]

ops[1] = 12
ops[2] = 2

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

print(ops)
