import heapq

def a_b(min_count, max_count):
    head = [(int(grid[0][1]), 0, 1, 0, 1), (int(grid[1][0]), 1, 0, 1, 1)]
    visited = {(0, 1, 0, 1), (1, 0, 1, 1)}
    m, n = len(grid), len(grid[0])
    offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    def is_valid(x, y):
        return x >= 0 and y >= 0 and x < m and y < n
    
    while head:
        cost, x, y, d, count = heapq.heappop(head)
        if (x, y) == (m - 1, n - 1) and count >= min_count:
            return cost
        if count < min_count:
            next_x, next_y = x + offsets[d][0], y + offsets[d][1]
            if not is_valid(next_x, next_y):
                continue
            new_cost = cost + int(grid[next_x][next_y])
            if (next_x, next_y, d, count + 1) not in visited:
                heapq.heappush(head, (new_cost, next_x, next_y, d, count + 1))
                visited.add((next_x, next_y, d, count + 1))
        else:
            for i, (off_x, off_y) in enumerate(offsets):
                if off_x + offsets[d][0] == 0 and off_y + offsets[d][1] == 0:
                    continue
                next_x, next_y = x + off_x, y + off_y
                if count == max_count and i == d or not is_valid(next_x, next_y):
                    continue
                new_cost = cost + int(grid[next_x][next_y])
                new_count = count + 1 if i == d else 1
                if (next_x, next_y, i, new_count) not in visited:
                    heapq.heappush(head, (new_cost, next_x, next_y, i, new_count))
                    visited.add((next_x, next_y, i, new_count))

if __name__ == '__main__':
    with open('input17.txt', 'r') as f:
        grid = f.read().split()
    m, n = len(grid), len(grid[0])
    min_count_a, max_count_a = 0, 3
    min_count_b, max_count_b = 4, 10
    print(a_b(min_count_a, max_count_a))
    print(a_b(min_count_b, max_count_b))
