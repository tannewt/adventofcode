import sys

def calculate_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel < 0:
        return 0
    return fuel + calculate_fuel(fuel)

total_fuel = 0
with open(sys.argv[1], "r") as f:
    for mass in f.readlines():
        mass = int(mass.strip())
        fuel = calculate_fuel(mass)
        print(mass, fuel)
        total_fuel += fuel

print(total_fuel)
