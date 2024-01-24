with open("input20.txt", "r") as file:
    broadcasters, conjunctions, flipflops, relevant, queue, low, high, button, p2 = {}, {}, {}, {}, {"rx"}, 0, 0, 0, 1
    for broadcaster, receivers in [x.split(" -> ") for x in file.read().splitlines()]:
        b, receivers = broadcaster[1:], receivers.split(", ")
        if broadcaster == "broadcaster":  broadcasters[broadcaster] = {x : (lambda y: y) for x in receivers}
        elif broadcaster.startswith("&"): broadcasters[b] = {x : (lambda y, b=b: set(conjunctions[b].values()) != {1}) for x in receivers}; conjunctions[b] = {}
        elif broadcaster.startswith("%"): broadcasters[b] = {x : (lambda y, b=b: flipflops[b])                         for x in receivers}; flipflops[b] = 0
    for k, v in broadcasters.items():
        for x in v:
            if x in conjunctions: conjunctions[x][k] = 0
    while queue:
        current = queue.pop()
        relevant[current] = nxt = [k for k, v in broadcasters.items() if current in v]
        for x in nxt:
            if x not in relevant: queue.add(x)
    conj_patterns = {x for x in set(sum(relevant.values(), [])) if x in conjunctions}
    while conj_patterns:
        button += 1; low += 1
        queue = [{"broadcaster" : (0, "button")}]
        while queue:
            receiver, (signal, origin) = queue.pop(0).popitem()
            if receiver not in broadcasters: continue
            if receiver in conjunctions: conjunctions[receiver][origin] = signal
            if receiver in flipflops:
                if signal: continue
                else: flipflops[receiver] = not flipflops[receiver]
            for remote, signal_func in broadcasters[receiver].items():
                queue.append({remote : (sent := signal_func(signal), receiver)})
                if sent == 1: high += 1
                else:         low += 1
            if receiver in conj_patterns and sent: conj_patterns.remove(receiver); p2 *= button
        if button == 1000: p1 = low * high
    print(p1, p2)
