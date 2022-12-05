import sys

from collections import defaultdict
from copy import deepcopy

INPUT = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

if len(sys.argv) > 1:
    INPUT = open(sys.argv[1]).read()

MAP, INSTRUCTION = INPUT.split("\n\n")

stacks = defaultdict(list)

for line in MAP.splitlines():
    if "[" in line:
        for i, s in enumerate(range(1, len(line), 4)):
            if line[s].strip():
                stacks[i+1].append(line[s])

stacks = {
    k: list(reversed(v))
    for k, v in stacks.items()
}
stacks2 = deepcopy(stacks)

for line in INSTRUCTION.splitlines():
    if "move" in line:
        instruction = line.split()
        num, fr, to = int(instruction[1]), int(instruction[3]), int(instruction[5])

        for i in range(num):
            stacks[to] += stacks[fr].pop()

st1 = ""
for i in range(len(stacks)):
    st1 += stacks[i+1][-1]
print(st1)

for line in INSTRUCTION.splitlines():
    if "move" in line:
        instruction = line.split()
        num, fr, to = int(instruction[1]), int(instruction[3]), int(instruction[5])
        
        rem = stacks2[fr][-num:]
        stacks2[fr] = stacks2[fr][:-num]
        stacks2[to] += rem
st2 = ""
for i in range(len(stacks2)):
    st2 += stacks2[i+1][-1]

print(st2)

