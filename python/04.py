with open('04.txt') as f:
    INPUT = f.readlines()

part1 = 0
part2 = 0

for line in INPUT:
    a, b = line.split(",")
    (a1, a2), (b1, b2) = a.split("-"), b.split("-")
    r_a = range(int(a1), int(a2)+1)
    r_b = range(int(b1), int(b2)+1)

    part1 += int(any((
        all((n_a in r_b for n_a in r_a)),
        all((n_b in r_a for n_b in r_b)),
    )))
    part2 += int(any((
        any((n_a in r_b for n_a in r_a)),
        any((n_b in r_a for n_b in r_b)),
    )))
print(part1, part2)
