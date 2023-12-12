file = 'input12.txt'
lines = [line for line in open(file).read().rstrip().split('\n')]
output=0
pos_cache = {}

def return_groups(string):
    return tuple(map(int, string.split(',')))


def possibilities(springs, groups):
    global pos_cache

    if hash(str(springs) + str(groups)) in pos_cache.keys():
        return pos_cache[hash(str(springs) + str(groups))]['counter']

    if not groups:
        if '#' not in springs:
            return 1
        return 0

    cntr = 0
    for position in range(len(springs) - sum(groups[1:]) + len(groups[1:]) - groups[0] + 1):
        possible = '.' * position + '#' * groups[0] + '.'
        
        for spring, possible_spring in zip(springs, possible):
            if spring != possible_spring and spring != '?':
                break
        else:
            cntr += possibilities(springs[len(possible):], groups[1:])

    pos_cache[hash(str(springs) + str(groups))] = {
        'counter': cntr
    }
    return cntr


# part 1
for line in lines:
    springs, groups = line.split()[0], return_groups(line.split()[1])
    output += possibilities(springs, groups)

print(output) 

output = 0

# part 2
for line in lines:
    springs, groups = line.split()[0], return_groups(line.split()[1])
    output += possibilities('?'.join((springs,) * 5), groups * 5)

print(output)
