def main(puzzle_input):
    # Parse the input
    puzzle_input = puzzle_input.splitlines()
    sum = 0
    for module in puzzle_input:
        sum += (int(int(module)/3)) - 2
    return sum


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
