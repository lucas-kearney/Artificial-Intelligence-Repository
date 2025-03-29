from collections import deque

class Graph:
    #example of adjacency list (or rather map)
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n, time):
        if time < 2 or time > 7:
            H = {
            'Start': 1, 'Goal': 1,
            '8th 41st': 2, '8th 42nd': 1, '8th 43rd': 2, '8th 44th': 2, '8th 45th': 2,
            '9th 41st': 2, '9th 42nd': 1, '9th 43rd': 2, '9th 44th': 2, '9th 45th': 2,
            '10th 41st': 2, '10th 42nd': 1, '10th 43rd': 2, '10th 44th': 2, '10th 45th': 2, '10th 46th': 2, '10th 47th': 2,
            '11th 42nd': 1, '11th 43rd': 2, '11th 44th': 2, '11th 45th': 2, '11th 46th': 2, '11th 47th': 2
        }
        else:
            H = {
            'Start': 1, 'Goal': 1,
            '8th 41st': 4, '8th 42nd': 6, '8th 43rd': 4, '8th 44th': 4, '8th 45th': 4,
            '9th 41st': 4, '9th 42nd': 6, '9th 43rd': 4, '9th 44th': 4, '9th 45th': 4,
            '10th 41st': 6, '10th 42nd': 6, '10th 43rd': 4, '10th 44th': 4, '10th 45th': 2, '10th 46th': 4, '10th 47th': 4,
            '11th 42nd': 6, '11th 43rd': 4, '11th 44th': 4, '11th 45th': 4, '11th 46th': 2, '11th 47th': 4
        }
        return H.get(n, 1)

    def a_star_algorithm(self, start_node, stop_node, time):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v, time) < g[n] + self.h(n, time):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    
    
Homework3_map = {
    'Start' : [('8th 41st', 1), ('8th 43rd', 1), ('9th 42nd', 3.5)],

    '8th 41st': [('8th 42nd', 1), ('9th 41st', 3.5)],
    '8th 42nd': [('8th 41st', 1), ('8th 43rd', 1), ('9th 42nd', 3.5)],
    '8th 43rd': [('8th 42nd', 1), ('8th 44th', 1), ('9th 43rd', 3.5)],
    '8th 44th': [('8th 43rd', 1), ('8th 45th', 1), ('9th 44th', 3.5)],
    '8th 45th': [('8th 44th', 1), ('9th 45th', 3.5)],
    
    '9th 41st': [('9th 42nd', 1), ('8th 41st', 3.5), ('10th 41st', 3.5)],
    '9th 42nd': [('9th 41st', 1), ('9th 43rd', 1), ('8th 42nd', 3.5), ('10th 42nd', 3.5)],
    '9th 43rd': [('9th 42nd', 1), ('9th 44th', 1), ('8th 43rd', 3.5), ('10th 43rd', 3.5)],
    '9th 44th': [('9th 43rd', 1), ('9th 45th', 1), ('8th 44th', 3.5), ('10th 44th', 3.5)],
    '9th 45th': [('9th 44th', 1), ('8th 45th', 3.5), ('10th 45th', 3.5)],
    
    '10th 41st': [('10th 42nd', 1), ('9th 41st', 3.5)],
    '10th 42nd': [('10th 41st', 1), ('10th 43rd', 1), ('9th 42nd', 3.5), ('11th 42nd', 3.5)],
    '10th 43rd': [('10th 42nd', 1), ('10th 44th', 1), ('9th 43rd', 3.5), ('11th 43rd', 3.5)],
    '10th 44th': [('10th 43rd', 1), ('10th 45th', 1), ('9th 44th', 3.5), ('11th 44th', 3.5)],
    '10th 45th': [('10th 44th', 1), ('10th 46th', 1), ('9th 45th', 3.5), ('11th 45th', 3.5)],
    '10th 46th': [('10th 45th', 1), ('10th 47th', 1), ('11th 46th', 3.5)],
    '10th 47th': [('10th 46th', 1), ('11th 47th', 3.5)],

    '11th 42nd': [('11th 43rd', 1), ('10th 42nd', 3.5)],
    '11th 43rd': [('11th 42nd', 1), ('11th 44th', 1), ('10th 43rd', 3.5)],
    '11th 44th': [('11th 43rd', 1), ('11th 45th', 1), ('10th 44th', 3.5)],
    '11th 45th': [('11th 44th', 1), ('11th 46th', 1), ('10th 45th', 3.5)],
    '11th 46th': [('11th 45th', 1), ('11th 47th', 1), ('10th 46th', 3.5)],
    '11th 47th': [('11th 46th', 1), ('10th 47th', 3.5)],

    '11th 46th': [('Goal', 3.5)]
}

time = int(input("Enter when you will be traveling in the afternoon: "))  
graph = Graph(Homework3_map)
graph.a_star_algorithm('Start', 'Goal', time)
    