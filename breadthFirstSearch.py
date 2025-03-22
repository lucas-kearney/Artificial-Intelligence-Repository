from collections import deque

class Node:
    def __init__(self, value):
        self.value = value  # Node value
        self.children = []  # List of child nodes

    def add_child(self, child_node):
        self.children.append(child_node)

class BFS:
    def __init__(self, root):
        self.root = root  # The root node of the tree

    def bfs_search(self, target_value):
        # Create a queue for BFS
        open = deque([self.root])
        
        # Create a set to track visited nodes (optional in tree, as there are no cycles)
        closed = set()
        
        while open:
            # Dequeue the next node from the queue
            current_node = open.popleft()
            
            print(f"Visiting node : {current_node.value}")

            if current_node.value == target_value:
                return current_node
            
            # Add all children of the current node to the queue
            for child in current_node.children:
                if child not in closed:
                    closed.add(child)
                    open.append(child)

        return None

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G1 = Node("G1")
H = Node("H")
I = Node("I")
J = Node("J")
K = Node("K")
L = Node("L")
M = Node("M")
N = Node("N")
G2 = Node("G2")

A.add_child(B)
A.add_child(C)
B.add_child(D)
B.add_child(E)
C.add_child(F)
C.add_child(H)
D.add_child(I)
D.add_child(J)
E.add_child(K)
E.add_child(G1)
F.add_child(L)
F.add_child(M)
H.add_child(G2)
H.add_child(N)
        
bfs_instance = BFS(A)
found_node = bfs_instance.bfs_search("F")

if found_node:
    print(f"Node with value '{found_node.value}' found.")
else:
    print("Node not found.")