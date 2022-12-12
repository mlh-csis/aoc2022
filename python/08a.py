import sys

INPUT = """30373
25512
65332
33549
35390
""".strip()

if len(sys.argv) > 1:
    INPUT = open(sys.argv[1]).read()

INPUT = INPUT.splitlines()

# Calculate the perimeter of the grid
p1 = (len(INPUT) * 2) + (len(INPUT[0]) * 2) - 4

# Calculate the maximum value for each row and column in the grid
max_row = [max(row) for row in INPUT]
max_col = [max(INPUT[i][j] for i in range(len(INPUT))) for j in range(len(INPUT[0]))]

p2 = 0

for y in range(1, len(INPUT) - 1):
    for x in range(1, len(INPUT[y]) - 1):
        tree = INPUT[y][x]

        # Check if any of the neighboring elements are smaller
        if (
            tree > max_row[y]
            or tree > max_row[y + 1]
            or tree > max_col[x]
            or tree > max_col[x + 1]
        ):
            p1 += 1

        left = 0
        stopleft = False
        right = 0
        stopright = False
        top = 0
        stoptop = False
        bottom = 0
        stopbottom = False

        for i in range(1, len(INPUT)):
            if x - i >= 0 and not stopleft:
                left += 1
                if INPUT[y][x - i] >= tree:
                    stopleft = True

            if x + i < len(INPUT[x]) and not stopright:
                right += 1
                if INPUT[y][x + i] >= tree:
                    stopright = True

            if y - i >= 0 and not stoptop:
                top += 1
                if INPUT[y - i][x] >= tree:
                    stoptop = True

            if y + i < len(INPUT) and not stopbottom:
                bottom += 1
                if INPUT[y + i][x] >= tree:
                    stopbottom = True

            score = top * left * right * bottom
            if score > p2:
                p2 = score

print("p1", p1)
print("p2", p2)
