def fuel_calculation(weight):
    sum = (int(weight/3)) - 2
    if sum < 0:
        sum = 0
    return sum

def main(puzzle_input):
    # Parse the input
    module_fuel = 0
    total_fuel = 0
    for module in puzzle_input:
        module_fuel = fuel_calculation(module)
        fuel_fuel = module_fuel
        # negative fuel
        while fuel_fuel > 0:
            fuel_fuel = fuel_calculation(fuel_fuel)
            module_fuel += fuel_fuel

        total_fuel += module_fuel

    return str(total_fuel)

puzzle_input = (100152,
121802,
140047,
92337,
101891,
122051,
50384,
53628,
139979,
57959,
90354,
119201,
53941,
74563,
140320,
69972,
90954,
85414,
52999,
69869,
65511,
91084,
146614,
120976,
145517,
121313,
99155,
144062,
53343,
60992,
81324,
109565,
83665,
100255,
116562,
71967,
66486,
76844,
83233,
129089,
98787,
118848,
120030,
123908,
144800,
113563,
74763,
80902,
58740,
115929,
57926,
61739,
118481,
111540,
55259,
90161,
110745,
85103,
92616,
126402,
71906,
137282,
76811,
124470,
140723,
89796,
98126,
127274,
104925,
120395,
134417,
105281,
140414,
52683,
149260,
123259,
125238,
68860,
103545,
90308,
118854,
121111,
72989,
62993,
96615,
145935,
75078,
96752,
118779,
68090,
95136,
82132,
149426,
51496,
70123,
129725,
63022,
74422,
143216,
139349)

print(main(puzzle_input))