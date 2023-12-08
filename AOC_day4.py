lines = open('C:\\Users\\hp\\OneDrive\\Desktop\\Code\\Advent_Of_Code_2023\\input4.txt', 'r').readlines()

total = 0
for i in lines:
    winning, given = map(str.split, i.split('|'))
    common = set(winning) & set(given)
    total += 2 ** (len(common) - 1) if common else 0
print(total) #Part 1



cards = [1] * len(lines)
for i, line in enumerate(lines):
    x, y = map(str.split, line.split('|'))
    n = len(set(x) & set(y))
    for j in range(i + 1,i + 1 + n):
        cards[j] += cards[i]
print(sum(cards)) #Part 2


