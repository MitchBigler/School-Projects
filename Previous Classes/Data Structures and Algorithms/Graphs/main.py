import math
import heapq

class Graph:
    class Vertex:
        def __init__(self, label):
            self.label = label

        def __str__(self):
            return self.label

    def __init__(self):
        self.adjacency_list = {} #adjacency list: key:value --> label:(to_;label, weight)
        self.vertices = {} #holds all vertices: key:value--> label: vertex object

    def __contains__(self, label):
        for v in self.vertices:
            if label == v:
                return True
        return False

    def add_vertex(self, label):
        # label is a string, otherwise raise ValueError
        if not isinstance(label, str):
            raise ValueError("label must be a string")

        # if len label > 1, raise ValueError for the project 8
        if len(label) > 1:
            raise ValueError("label must be a single character")

        if label in self.vertices:
            raise ValueError("label is already in graph")
        self.vertices[label] = self.Vertex(label)
        self.adjacency_list[label] = [] #(to_label, weight)
        return self

    def add_edge(self, from_label, to_label, weight=1.0):
        # Rais ValueError if from_label, to_label is not valid
        if from_label not in self.vertices:
            raise ValueError(f"{from_label} is not a valid vertex")
        # Raise ValueError if from_label or to_label not in the graph
        if to_label not in self.vertices:
            raise ValueError(f"{to_label} is not a valid vertex")
        if not isinstance(weight, (int, float)):  # Check if weight is numeric (int or float)
            raise ValueError(f"Weight must be a number, but got {type(weight)}")
        
        adjacent_vertices = self.adjacency_list.get(from_label)

        # edge (from_label, to_label) is in the graph, update the weight
        # i (to_label, weight)
        for index, i in enumerate(adjacent_vertices):
            if i[0] == to_label: # edge(from_label, to_label) already in the graph, update
                adjacent_vertices[index] = to_label, weight
                return self
            
        # otherwise add edge to the graph
        self.adjacency_list[from_label].append((to_label, weight))
        return self

    def add_undirected_edge(self, a_label, b_label, weight=1.0):
        self.add_edge(a_label, b_label, weight)
        self.add_edge(b_label, a_label, weight)

    def get_weight(self, from_label, to_label):
        ''' returns the weight of an edge or math.inf is no path
        if src or dest are not defined vertices, ValueError '''
        if from_label not in self:
            raise ValueError(f"{from_label} is not in the graph")
        if to_label not in self:
            raise ValueError(f"{to_label} is not in the graph")
        # adjacency_list
        # label:[(to_label1, weight1), (to_label2, weight2)]
        for lw in self.adjacency_list[from_label]:
            if lw[0] == to_label:
                return lw[1]
        return math.inf

    def __str__(self):
        # Output in GraphViz notation
        output = "digraph G {\n"
        for from_label, edges in self.adjacency_list.items():
            for to_label, weight in edges:
                output += f'   {from_label} -> {to_label} [label="{weight}",weight="{weight}"];\n'
        output += "}"
        return output

    def _get_neighbors(self, from_label):
        '''
        return: [] if there is no edge coming out of from_label
                [v1, v2, ....] an edge from from_label to any vertex in the returned list in alphabetic order
        '''
        if from_label not in self.vertices:
            raise ValueError("Vertex not in the graph")
        value = self.adjacency_list[from_label]
        if value:
            return [to_label for to_label, w in value]
        return []

    def bfs(self, starts):
        f_q = []
        f_q.append(starts)
        dis_set = set()
        dis_set.add(starts)
        while len(f_q) !=0:
            current = f_q.pop(0)
            yield current
            adj_vertex = self.adjacency_list[current]
            adj_vertex_list = self._get_neighbors(current)
            adj_vertex_list.sort() # sort in ascending order for project only

            if len(adj_vertex) > 0:
                for i in adj_vertex_list:
                    if i[0] not in dis_set:
                        f_q.append(i)
                        dis_set.add(i)

    def dfs(self, starts):

        stack = []
        stack.append(starts)
        visited_set = set()
        visited_set.add(starts)

        while stack:
            current = stack.pop()
            yield current

            adj_vertex_list = self._get_neighbors(current)
            adj_vertex_list.sort()

            # Explore all unvisited neighbors
            for neighbor in adj_vertex_list:
                if neighbor not in visited_set:
                    stack.append(neighbor)
                    visited_set.add(neighbor)

    def dsp(self, start, end):
        # Initialize pq and dicts
        pq = [(0, start)]
        dist = {start: 0}
        prev = {start: None}

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)

            # Exit if reached end
            if current_vertex == end:
                break

            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_dist + weight
                if neighbor not in dist or distance < dist[neighbor]:
                    dist[neighbor] = distance
                    prev[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))

        # Reconstruct path from start to end
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = prev.get(current)

        path.reverse()

        # Return distance, path
        return dist.get(end, math.inf), path


    def dsp_all(self, start):
        # Dict for shortest paths
        paths = {}

        # Run dsa for each vertex
        for vertex in self.vertices:
            distance, path = self.dsp(start, vertex)
            paths[vertex] = path

        return paths

def main():
    g = Graph()
    vertices = ["A", "B", "C", "D", "E", "F"]
    for vertex in vertices:
        g.add_vertex(vertex)

    edges = [
        ("A", "B", 2.0), ("A", "F", 9.0),
        ("B", "C", 8.0), ("B", "D", 15.0), ("B", "F", 6.0),
        ("C", "D", 1.0),
        ("E", "C", 7.0), ("E", "D", 3.0),
        ("F", "B", 6.0), ("F", "E", 3.0)
    ]
    for e in edges:
        g.add_edge(e[0], e[1], e[2]) # from, to, weight
    print(g)

    for e in edges:
        print(f"The weight of ({e[0]}, {e[1]}) is {g.get_weight(e[0], e[1])}")


if __name__ == "__main__":
    main()