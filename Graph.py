from queue import PriorityQueue


class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

    def pop_neighbor(self, neighbor):
        return self.neighbors.pop(neighbor)

    def __str__(self):
        return self.value


class Graph:
    def __init__(self):
        self.vertexes = {}

    def add_vertex(self, value):
        vertex = Vertex(value)
        self.vertexes[value] = vertex

    def get_neighbor(self, value):
        if value in self.vertexes.keys():
            vertex = self.vertexes[value]
            temp = ""
            for neighbor, weight in vertex.neighbors.items():
                temp += f"({neighbor.value} : {weight}), "
            return temp
        else:
            raise IndexError("Could not find vertex.")

    def connect(self, origin, destination, weight):
        if origin in self.vertexes.keys() and destination in self.vertexes.keys():
            self.vertexes[origin].add_neighbor(self.vertexes[destination], weight)
        else:
            if origin not in self.vertexes.keys():
                self.add_vertex(origin)
            if destination not in self.vertexes.keys():
                self.add_vertex(destination)
            self.connect(origin, destination, weight)

    def connect_to_getter(self, vertex1, vertex2, weight):
        self.connect(vertex1, vertex2, weight)
        self.connect(vertex2, vertex1, weight)

    def disconnect(self, origin, destination):
        if origin in self.vertexes.keys() and destination in self.vertexes.keys():
            self.vertexes[origin].pop_neighbor(self.vertexes[destination])
        else:
            raise IndexError("Could not find the vertex origin or destination")

    def __str__(self):
        temp = ""
        for value in self.vertexes.keys():
            temp += f"{value} => "
            temp += self.get_neighbor(value) + "\n"
        return temp

    def get_dict(self):
        temp = {}
        for vertex in self.vertexes.values():
            temp[vertex.value] = {}
            for neighbor, weight in vertex.neighbors.items():
                temp[vertex.value][neighbor.value] = weight
        return temp

    def ucs(self, start, goal):
        visited = set()
        queue = PriorityQueue()
        if start not in self.vertexes.keys() and goal not in self.vertexes:
            raise IndexError("Could not find start or goal.")
        queue.put((0, start, [start]))

        while not queue.empty():
            cost, node, path = queue.get()
            if node == goal:
                return cost, path
            if node not in visited:
                visited.add(node)
                for neighbor, weight in self.vertexes[node].neighbors.items():
                    if neighbor.value not in visited:
                        new_cost = cost + weight
                        new_path = path + [neighbor.value]
                        queue.put((new_cost, neighbor.value, new_path))
                    elif neighbor.value == goal:
                        if cost + weight < new_cost:
                            new_cost = cost + weight
                            new_path = path + [neighbor.value]
                            queue.put((new_cost, neighbor.value, new_path))
        return float('inf'), None


if __name__ == '__main__':
    test = Graph()
    test.add_vertex("A")
    test.add_vertex("B")
    test.add_vertex("C")
    test.add_vertex("D")
    test.add_vertex("E")
    test.add_vertex("F")
    test.connect("A", "B", 2)
    test.connect("A", "C", 1)
    test.connect("B", "E", 2)
    test.connect("B", "D", 3)
    test.connect("C", "E", 4)
    test.connect("D", "F", 4)
    test.connect("E", "F", 1)
    print(test.ucs("A", "F"))

