from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    @property
    def nodes(self):
        nodes = set()
        nodes.update(self.graph.keys())
        for node in self.graph.keys():
            for neighbor in self.graph[node]:
                nodes.add(neighbor)
        return list(nodes)

    def add_node(self, node):
        if node not in self.nodes:
            self.graph[node] = list()

    @property
    def edges(self):
        edges = list()
        for source, neighbors in self.graph.items():
            for neighbor in neighbors:
                edges.append((source, neighbor))
        return edges

    def add_edge(self, edge):
        node1, node2 = edge
        self.graph[node1].append(node2)

    def topological_util(self, node, visited, label):
        visited[node] = True
        for edge in self.graph[node]:
            if not visited[edge]:
                self.topological_util(edge, visited, label)
        label.appendleft(node)

    def topological_sort(self):
        visited = dict.fromkeys(self.nodes, False)
        # store all nodes in topological order, the index is the position
        label = deque()
        for node in self.nodes:
            if not visited[node]:
                self.topological_util(node, visited, label)
        return label