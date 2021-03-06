"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
import math
"""
Simple graph implementation compatible with BokehGraph class.
"""

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if self.x is None:
            self.x = random.randint(1,6) * (self.id+1) // 4
        if self.y is None:
            self.y = random.randint(1,6) * (self.id+1) % 4
        if self.value is None:
            self.value = self.id
        if self.color is None:
            hexValues = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            colorString = "#"
            for i in range(0, 6):
                colorString += hexValues[random.randint(0,len(hexValues) - 1)]
            # Algorithm for bright colors
            # colorArray = ["F"]
            # for i in range(0, 2):
            #     colorArray.append(hexValues[random.randint(0,len(hexValues) - 1)])
            # random.shuffle(colorArray)
            # colorString = "#" + "".join(colorArray)
            # print(colorString)
            self.color = colorString



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    
    def dft(self, initial_vert, visited=[]):
        # Visited checks if we've visited the node before (in this case, it's because we're using an undirected graph, so there's potential for the same node to be visited multiple times depending on the configuration of the edges)
        visited.append(initial_vert)
        # Establish that we've visited the node (print)
        print(self.vertices[initial_vert].value)
        # Call dft recursively on each child (if child has not been visited)
        for child_vert in self.vertices[initial_vert].edges:
            # Check if child has been visited
            if child_vert not in visited:
                # If not, call DFS
                self.dft(child_vert, visited)
    
    def dft_stack(self, initial_vertex_id):
        # Create empty queue
        stack = Stack()
        # Put initial vert in the queue
        stack.push(initial_vertex_id)
        # Declare visited list
        visited = []
        # While the queue is not empty...
        while stack.size() > 0:
            # ...remove the first item from the queue...
            v = stack.pop()
            # ...then if it has not been visited...
            if v not in visited:
                # ...print its value...
                print(self.vertices[v].value)
                visited.append(v) # ...mark as visited...
                # ...then put its children into the queue.
                for next_vert in self.vertices[v].edges:
                    stack.push(next_vert)

    def bft(self, initial_vertex_id):
        # Create empty queue
        q = Queue()
        # Put starting vert in the queue
        q.enqueue(initial_vertex_id)
        # Declare visited list
        visited = []
        # While the queue is not empty—
        while q.size() > 0:
            # ...remove the first item from the queue...
            vert = q.dequeue()
            # ... then if it hasn't been visited ...
            if vert not in visited:
                # ... print its value ...
                print(self.vertices[vert].value)
                visited.append(vert) # mark the vert as visited
                # then put its children into the queue
                for next_vert in self.vertices[vert].edges:
                    q.enqueue(next_vert)
    
    def dfs(self, initial_vert, target_value, visited=[]):
        visited.append(initial_vert)
        if self.vertices[initial_vert].value == target_value:
            return True
        for child_vert in self.vertices[initial_vert].edges:
            if child_vert not in visited:
                if self.dfs(child_vert, target_value, visited):
                    return True
        return False
    
    def dfs_path(self, initial_vert, target_value, visited=[], path=[]):
        visited.append(initial_vert)
        path = path + [initial_vert]
        if self.vertices[initial_vert].value == target_value:
            return path
        for child_vert in self.vertices[initial_vert].edges:
            if child_vert not in visited:
                new_path = self.dfs_path(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None
    

    def bfs(self, initial_vert, target_value):
        q = Queue()
        q.enqueue(initial_vert)
        visited = []
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                if self.vertices[v].value == target_value:
                    return True
                visited.append(v) # ... mark as visited ...
                for next_vert in self.vertices[v].edges:
                    q.enqueue(next_vert)
        return False
    
    def bfs_path(self, initial_vert, target_value):
        q = Queue()
        q.enqueue([initial_vert])
        visited = []
        while q.size() > 0:
            print(q.queue)
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                if self.vertices[v].value == target_value:
                    return path
                visited.append(v) #...mark as visited...
                for next_vert in self.vertices[v].edges:
                    # q.enqueue(next_vert)
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        return None


