class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def reverse(self):
        return Edge(self.v, self.u)

    def __str__(self):
        return f"({self.u}, {self.v})"

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = {}
        for v in vertices:
            self.edges[v] = []

    def add_edges(self, lst):
        for l in lst:
            self.add_edge(l)

    def add_edge(self, e):
        self.edges[e.u].append(e)
        self.edges[e.v].append(e.reverse())

    def __str__(self):
        str = ""
        for vertex in self.vertices:
            str += f"{vertex}->"
            for e in self.edges[vertex]:
                str += f"({e.u},{e.v}), "
            str += "\n"
        return str

def spanning_tree(graph):
    s_vertices = []
    s_edges = []
    for vertex in graph.vertices:
        if vertex not in s_vertices:
            s_vertices.append(vertex)
            for edge in graph.edges[vertex]:
                if edge.v not in s_vertices:
                    s_edges.append(edge)
    span_tree = Graph(s_vertices)
    span_tree.add_edges(s_edges)
    return span_tree


if __name__ == "__main__":
    v = list(range(5))
    g = Graph(v)
    g.add_edges([Edge(0, 1), Edge(0, 2), Edge(1, 4), Edge(2, 4), 
                 Edge(2, 3), Edge(3, 4)])
    print(g)

    print(spanning_tree(g))