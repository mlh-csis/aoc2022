with open('03.txt','r') as f:
    INPUT = f.read().strip().splitlines()

lower_chars = "abcdefghijklmnopqrstuvwxyz"
CHARS = lower_chars + lower_chars.upper()

score = 0
for line in INPUT:
    split_at = int(len(line)/2)
    a, b = line[0:split_at], line[split_at:len(line)]
    for c in a:
        if c in b:
            s = CHARS.index(c) + 1
            score += s
            break
print(score)    

i = 0
score2 = 0
while i < len(INPUT):
    for a in INPUT[i]:
        if a in INPUT[i+1] and a in INPUT[i+2]:
            s = CHARS.index(a) + 1
            score2 += s
            i += 3
            break
print(score2)
