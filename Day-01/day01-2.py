def fuel_calculation(weight):
    sum = (int(weight/3)) - 2
    if sum < 0:
        sum = 0
    return sum

def main(puzzle_input):
    # Parse the input

    puzzle_input = puzzle_input.splitlines()
    module_fuel = 0
    total_fuel = 0
    for module in puzzle_input:
        module_fuel = fuel_calculation(int(module))
        fuel_fuel = module_fuel
        # negative fuel
        while fuel_fuel > 0:
            fuel_fuel = fuel_calculation(fuel_fuel)
            module_fuel += fuel_fuel

        total_fuel += module_fuel

    return str(total_fuel)

def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
