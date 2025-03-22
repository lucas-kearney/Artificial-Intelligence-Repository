class Node:
    def __init__(self, name):  # initialization method
        self.name = name #fields
        self.children = []

    def add_child(self, child): #connections to each leaf or node
        self.children.append(child)

def depth_first_search(start, goal):
    open_list = [start]  # LIFO stack for DFS
    closed = set()

    while open_list: #while we have something in the stack
        node = open_list.pop() #remove and analyze what this node links to

        if node.name in closed: 
            continue
        print(f"Visiting: {node.name}")

        if node.name == goal:
            print(f"Goal {goal} found!")
            return node
        
        closed.add(node.name)  # Mark node as visited
        open_list.extend(reversed(node.children))  # Add children in reverse order

    print("Goal not found in tree.")
    return None

# Constructing the tree
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

# Conduct DFS
solution = depth_first_search(A, "F")
print("Using Depth First Search, the answer is:", solution.name if solution else "Not Found")