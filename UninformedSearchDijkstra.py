from collections import defaultdict

class Graph(): #class to store the node tree
    def __init__(self): #elf is being initialized as a dict
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list) #list of each leaf of the tee
        self.weights = {} #ability to input weights
    
    def add_edge(self, from_node, to_node, weight): #function to add leafs and create connections to nodes
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node) #adds new node to the end of the node before
        self.edges[to_node].append(from_node) #creates doubly linked version
        self.weights[(from_node, to_node)] = weight #weights between the two nodes are the same and both can be registered
        self.weights[(to_node, from_node)] = weight #either way you are traversing

def dijkstra(graph, initial, end): #shortest path algorithm
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial 
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        print(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

graph = Graph()

edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 6),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 3),
    ('F', 'H', 3),
    ('G', 'H', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('K', 'Y', 5),
]

for edge in edges:
        graph.add_edge(*edge)

shortest_path = dijkstra(graph, 'X', 'F')
print("Shortest path from X to F: ", shortest_path)