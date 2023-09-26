import re
from queue import PriorityQueue
import numpy as np

class Graph():
    def __init__(self):
        self.nodes = []
        self.translate = {}
        self.edges = []
        self.node_weight = {}
        self.edge_weight = {}
    
    def add_node(self, node: str, value: int):
        self.nodes.append(node)
        self.translate[node] = self.nodes.index(node)
        self.node_weight[node] = value
    
    def set_edges(self):
        num = len(self.nodes)
        self.edges = [[-1 for i in range(num)] for j in range(num)]
    
    def add_edge(self, a, b, weight):
        x = self.translate[a]
        y = self.translate[b]
        self.edges[x][y] = weight

    def reset_visited(self):
        self.visited = []

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(len(graph.nodes))}
    start_vertex = graph.translate[start_vertex]
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))
    visited = []
    e = graph.edges

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in range(len(graph.nodes)):
            if e[current_vertex][neighbor] != -1:
                distance = e[current_vertex][neighbor]
                if neighbor not in visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()
    graph_all = Graph()
    graph = Graph()

    start_node = "AA"

    for line in lines:
        value = [int(d) for d in re.findall(r'-?\d+', line)][0]
        graph_all.add_node(line[6:8], value)
        if value > 0 or line[6:8] == start_node:
            graph.add_node(line[6:8], value)
    
    graph_all.set_edges()
    graph.set_edges()

    nodes = graph_all.nodes
    for i in range(len(lines)):
        check = lines[i].split(";")[1]
        for n in nodes:
            if n in check:
                graph_all.add_edge(nodes[i], n, 1)

    reverse_translate = {v: k for k, v in graph_all.translate.items()}
    for node in nodes:
        D = dijkstra(graph_all, node)
        for vertex in range(len(D)):
            v = reverse_translate[vertex]
            if v in graph.nodes and node in graph.nodes:
                graph.add_edge(node, v, D[vertex])

    all = graph.edges
    start_index = graph.translate[start_node]
    max = 0
    steps = 0
    print(start_index)
        
main()