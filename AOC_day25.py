import sys
from itertools import combinations
from collections import defaultdict
import random
from heapq import heappop, heappush


class PartsGraph:
    def __init__(self, parts_list: list[str]) -> int:
        self.nodes = defaultdict(set)
        self.shortest_paths = dict()
        for part in parts_list:
            part, adjacent = part.split(":")
            adjacent = adjacent.strip()
            adjacent_parts = adjacent.split(" ")
            self.nodes[part].update(adjacent_parts)
            for adjacent_part in adjacent_parts:
                self.nodes[adjacent_part].add(part)

    def shortest_path(self, origin: str, destination: str) -> None:
        if (origin, destination) in self.shortest_paths:
            return
        queue = [(0, [origin])]
        distance = 0
        visited = set([origin])
        while queue:
            distance, path = heappop(queue)
            distance += 1
            vertex = path[-1]
            neighbours = [node for node in self.nodes[vertex] if node not in visited]
            for neighbour in neighbours:
                visited.add(neighbour)
                if neighbour == destination:
                    self.shortest_paths[(origin, destination)] = path + [neighbour]
                    return
                heappush(queue, (distance, path + [neighbour]))

    def compute_bridges(self) -> int:
        nodes = list(self.nodes.keys())
        for _ in range(200):
            origin, destination = random.sample(nodes, 2)
            self.shortest_path(origin, destination)
        edges = defaultdict(int)
        for pair in self.shortest_paths:
            for index in range(len(self.shortest_paths[pair]) - 1):
                vertices = sorted(self.shortest_paths[pair][index : index + 2])
                edges[(vertices[0], vertices[1])] += 1
        sorted_edges = list(edges.keys())
        sorted_edges.sort(key=lambda edge: edges[edge], reverse=True)

        # I'm gonna bet that the edges are within the first 10 of this list
        to_test = sorted_edges[:10]
        for edge_1, edge_2, edge_3 in combinations(to_test, 3):
            result = self.count(set([edge_1, edge_2, edge_3]))
            if result != 0:
                return result

    def count(self, ignore_edges: set[tuple[str, str]]) -> int:
        ignored_edges = list(ignore_edges)
        for edge in ignored_edges:
            ignore_edges.add((edge[1], edge[0]))
        vertex = list(self.nodes.keys())[0]
        queue = [vertex]
        visited = set([vertex])
        while queue:
            vertex = queue.pop()
            neighbours = [
                node
                for node in self.nodes[vertex]
                if node not in visited and (vertex, node) not in ignore_edges
            ]
            queue.extend(neighbours)
            visited.update(neighbours)
        return len(visited) * (len(self.nodes) - len(visited))


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input25.txt"
    part_list = open(file_name).read().strip().splitlines()
    parts_graph = PartsGraph(part_list)
    result = parts_graph.compute_bridges()
    print(f"The product of the sizes of the groups is {result}")
