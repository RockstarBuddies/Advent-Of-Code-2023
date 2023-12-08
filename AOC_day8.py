from math import lcm
with open("C:\\Users\\hp\\OneDrive\\Desktop\\Code\\Advent_Of_Code_2023\\input8.txt") as input:
    directions, paths = input.read().split('\n\n')
    paths = {k.strip():v[2:-1].replace(' ','').split(',') for k,v in (line.split('=') for line in paths.splitlines())}
    starts = [k for k in paths if k.endswith('A')]
def steps(s):
    c = 0
    while s[-1] != 'Z':
        d = directions[c%len(directions)]
        s = paths[s][d =='R']
        c += 1
    return c
print(steps('AAA')) #Part 1
print(lcm(*map(steps,starts))) #Part 2
