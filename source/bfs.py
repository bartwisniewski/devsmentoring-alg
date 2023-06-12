

class BFS:
    def __init__(self, graph, start_id, callback):
        self.graph = graph
        self.visited = []
        self.callback = callback
        self.stack = [start_id]

    def get_unvisited_neighbours(self, id):
        neighbours = self.graph.get_neighbours(id)
        unvisited = [neighbour for neighbour in neighbours if neighbour not in self.visited
                     and neighbour not in self.stack]
        return unvisited

    def step(self):
        active_id = self.stack.pop(0)
        self.visited.append(active_id)
        self.callback(active_id)
        self.stack += self.get_unvisited_neighbours(active_id)

    def run(self):
        while self.stack:
            self.step()




