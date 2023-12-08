
from collections import Counter

with open("C:\\Users\\hp\\OneDrive\\Desktop\\Code\\Advent_Of_Code_2023\\input7.txt") as f:
    data = f.read().strip()


def hand_type(hand):
    c = Counter(hand)
    
    counts = [0] if (jokers := c.pop("*", 0)) == 5 else sorted(c.values())
    
    counts[-1] += jokers
    match counts:
        case *_, 5:
            return 7
        case *_, 4:
            return 6
        case *_, 2, 3:  
            return 5
        case *_, 3:
            return 4
        case *_, 2, 2:
            return 3
        case *_, 2:
            return 2
    return 1


def solve(data):
    ws = [l.split() for l in data.split("\n")]
    return sum(rank * bid for rank, (*_, bid) in enumerate(sorted((hand_type(hand), *map("*23456789TJQKA".index, hand), int(bid)) for hand, bid in ws),1,))


#Part 1
print(solve(data))

#Part 2
print(solve(data.replace("J", "*")))
'''

import collections as c;L='J23456789TQKA';print(sum(r*int(b)for r,(*_,b)in enumerate(sorted((max(sorted(c.Counter(h.replace('J',l)).values())[::-1]for l in L),[*map(L.index,h)],b)for h,b in map(str.split,open("C:\\Users\\hp\\OneDrive\\Desktop\\Code\\input7.txt"))),1)))


'''
