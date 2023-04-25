import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

def heuristic_cost_estimate(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def a_star_search(graph, start, goal):
    closed_set = set()
    open_set = [start]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: g_score[start] + heuristic_cost_estimate(start, goal)}

    while open_set:
        current = min(open_set, key=lambda node: f_score[node])
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in graph.edges[current]:
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + graph.weights[(current, neighbor)]

            if neighbor not in open_set:
                open_set.append(neighbor)
            elif tentative_g_score >= g_score[neighbor]:
                continue

            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + heuristic_cost_estimate(neighbor, goal)

    return []

# Example usage:
graph = Graph()
graph.add_edge((0, 0), (1, 0), 1)
graph.add_edge((1, 0), (2, 0), 1)
graph.add_edge((2, 0), (2, 1), 1)
graph.add_edge((2, 1), (2, 2), 1)
graph.add_edge((2, 2), (1, 2), 1)
graph.add_edge((1, 2), (0, 2), 1)
graph.add_edge((0, 2), (0, 1), 1)
graph.add_edge((0, 1), (0, 0), 1)

start = (0, 0)
goal = (2, 2)
path = a_star_search(graph, start, goal)
print(f"Shortest path from {start} to {goal}: {path}")
