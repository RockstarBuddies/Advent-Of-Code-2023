infile = open("input19.txt")

#Part 1
wf = {}
for rule in infile:
    rule = rule.strip()
    if len(rule) == 0:
        break

    name, rest = rule.split("{")
    steps = rest.split("}")[0]
    steps = steps.split(",")

    wf[name] = []
    for step in steps:
        if not ":" in step:
            wf[name].append(["", "ALWAYS", 0, step])
            break
        step, dest = step.split(":")
        p = step[0]
        op = step[1]
        v = int(step[2:])
        wf[name].append([p, op, v, dest])

total = 0
for part in infile:
    part = part.strip()
    name = "in"
    vals = dict(x.split("=") for x in part[1:-1].split(","))
    pos = 0
    while name != "A" and name != "R":
        p, op, v, dest = wf[name][pos]

        if op == "ALWAYS":
            name = dest
            pos = 0
            continue
        elif op == ">":
            if int(vals[p]) > v:
                name = dest
                pos = 0
            else:
                pos += 1
        elif op == "<":
            if int(vals[p]) < v:
                name = dest
                pos = 0
            else:
                pos += 1

    print(part, name)
    if name == "A":
        total += sum(map(int, vals.values()))

print(total)

#Part 2
wf = {}
for rule in infile:
    rule = rule.strip()
    if len(rule) == 0:
        break

    name, rest = rule.split("{")
    steps = rest.split("}")[0]
    steps = steps.split(",")

    wf[name] = []
    for step in steps:
        if not ":" in step:
            wf[name].append(["", "ALWAYS", 0, step])
            break
        step, dest = step.split(":")
        p = step[0]
        op = step[1]
        v = int(step[2:])
        wf[name].append([p, op, v, dest])

all_range = frozenset(range(1,4001))

def poss(name, incoming):
    if name == "R":
        return 0
    if name == "A":
        return len(incoming["x"]) * len(incoming["m"]) * len(incoming["a"]) * len(incoming["s"])

    total = 0
    wff = wf[name]
    range_left = dict((k, set(v)) for (k, v) in incoming.items())
    for i in range(len(wff)):
        p, op, v, dest = wf[name][i]

        if op == "ALWAYS":
            total += poss(dest, range_left)
            break
        elif op == ">":
            rng = range(v+1, 4001)
        elif op == "<":
            rng = range(1, v)
        else:
            assert(False)

        sending = {}
        for sk, sv in range_left.items():
            if sk != p:
                sending[sk] = sv
            else:
                sending[sk] = set()
                for i in rng:
                    if i in sv:
                        sv.remove(i)
                        sending[sk].add(i)
        total += poss(dest, sending)

    return total


result = poss("in", {"x": all_range, "m": all_range, "a": all_range, "s": all_range})

print(result)
