import sys

INPUT = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
if len(sys.argv) > 1:
    INPUT = open(sys.argv[1]).read()

sop = 0
som = 0
for i in range(len(INPUT)):
    if len(set(INPUT[i : i + 4])) == 4:
        sop = i + 4
        break

for i in range(sop, len(INPUT)):
    if len(set(INPUT[i : i + 14])) == 14:
        som = i + 14
        break

print(sop, som)
