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

p1 = (len(INPUT) * 2) + (len(INPUT[0]) * 2) - 4
p2 = 0

for y in range(1, len(INPUT) - 1):
    for x in range(1, len(INPUT[y]) - 1):
        tree = INPUT[y][x]
        from_left = max(INPUT[y][:x])
        from_right = max(INPUT[y][x + 1 :])
        from_top = max(INPUT[i][x] for i in range(0, y))
        from_bottom = max(INPUT[i][x] for i in range(y + 1, len(INPUT)))

        if any(dir < tree for dir in (from_right, from_bottom, from_top, from_left)):
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
