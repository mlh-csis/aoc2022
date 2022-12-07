import sys
from copy import copy

INPUT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".strip().splitlines()

if len(sys.argv) > 1:
    INPUT = open(sys.argv[1]).read().splitlines()

INPUT = list(reversed(INPUT))
dirs = list()
current_dir = list()


def calc_size():
    while True:
        if len(INPUT) == 0:
            break

        entry = INPUT.pop()
        if entry.startswith("$ cd "):
            dir = entry[5:]
            if dir == "..":
                _ = current_dir.pop()
                return
            else:
                current_dir.append(dir)
                calc_size()
        elif entry.startswith("$ ls"):
            size = 0
            while True:
                if len(INPUT) == 0 or INPUT[-1].startswith("$"):
                    dirs.append(
                        ("".join(current_dir), size),
                    )
                    break
                entry = INPUT.pop()
                a, _ = entry.split()
                if a != "dir":
                    size += int(a)


calc_size()

p1 = 0
usage = sum(s for _, s in dirs)
need = 30000000
avail = 70000000 - usage
target = need - avail
p2 = 70000000

for d, _ in dirs:
    s = sum([s for a, s in dirs if a.startswith(d)])
    if s < 100000:
        p1 += s
    if s > target and s < p2:
        p2 = s

print("Part 1", p1)
print("Part 2", p2)
