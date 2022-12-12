import sys

INPUT = open(sys.argv[1]).read()

tail_pos = []
hx = 0
tx = 0
hy = 0
ty = 0

for line in INPUT.splitlines():
    dir, amount = line[0], int(line[2:])

    for step in range(amount):
        match dir:
            case "U":
                hy += 1
            case "D":
                hy -= 1
            case "R":
                hx += 1
            case "L":
                hx -= 1

        if abs(hx - tx) > 1:
            dx = hx - tx
            if dx < 0:
                dx = -1
            else:
                dx = 1
            tx += dx
            if ty != hy:
                ty = hy

        if abs(hy - ty) > 1:
            dy = hy - ty
            if dy < 0:
                dy = -1
            else:
                dy = 1
            ty += dy
            if tx != hx:
                tx = hx

        tail_pos.append((tx, ty))

print(len(set(tail_pos)))


rope = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
]


tail_pos_p2 = []

for line in INPUT.splitlines():
    dir, amount = line[0], int(line[2:])

    for step in range(amount):
        match dir:
            case "U":
                rope[0][1] += 1
            case "D":
                rope[0][1] -= 1
            case "R":
                rope[0][0] += 1
            case "L":
                rope[0][0] -= 1

        for i in range(1, len(rope)):
            if abs(rope[i - 1][0] - rope[i][0]) > 1:
                dx = rope[i - 1][0] - rope[i][0]
                if dx < 0:
                    dx = -1
                else:
                    dx = 1
                rope[i][0] += dx
                if rope[i][1] != rope[i - 1][1]:
                    rope[i][1] = rope[i - 1][1]

            if abs(rope[i - 1][1] - rope[i][1]) > 1:
                dy = rope[i - 1][1] - rope[i][1]
                if dy < 0:
                    dy = -1
                else:
                    dy = 1
                rope[i][1] += dy
                if rope[i][0] != rope[i - 1][0]:
                    rope[i][0] = rope[i - 1][0]

        tail_pos_p2.append((rope[9][0], rope[9][1]))
    print(repr(rope))

print(len(set(tail_pos_p2)))
