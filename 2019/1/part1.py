import sys

total_fuel = 0
with open(sys.argv[1], "r") as f:
    for mass in f.readlines():
        mass = int(mass.strip())
        fuel = (mass // 3) - 2
        print(mass, fuel)
        total_fuel += fuel

print(total_fuel)
