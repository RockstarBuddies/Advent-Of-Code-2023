import math
#Part 1
print(math.prod(sum(i * (limit - i) > distance for i in range(distance)) for limit, distance in zip([62, 73, 75, 65], [644, 1023, 1240, 1023])))

#Part 2
limit, distance = 62737565,644102312401023
print(sum(i * (limit - i) > distance for i in range(limit)))



