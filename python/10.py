import sys

INPUT = """noop
addx 3
addx -5
""".strip().splitlines()

if len(sys.argv) > 1:
    INPUT = open(sys.argv[1]).read().splitlines()

INPUT.reverse()

cycle = 1
X = 1
instruction = None
instruction_at = 0
signals = []
output = ""

while True:
    if not instruction:
        if len(INPUT) == 0:
            break
        line = INPUT.pop()
        if line.startswith("noop"):
            instruction_at = cycle
            instruction = lambda x: x
        else:
            instruction_at = cycle + 1
            instruction = lambda x: x + int(line[5:])

    if cycle in (20, 60, 100, 140, 180, 220):
        signals.append(cycle * X)

    if (cycle % 40 - 1) in (X - 1, X, X + 1):
        output += "#"
    else:
        output += "."

    if cycle % 40 == 0:
        output += "\n"

    if cycle == instruction_at:
        X = instruction(X)
        instruction = None

    cycle += 1

print(sum(signals))
print(output)
