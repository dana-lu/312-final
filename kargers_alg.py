# 312 Final Project - Karger's Min-Cut Algorithm

import numpy as np
import copy

'''
This class represents a graph data structure with data intialized from a file
'''
class Graph:
    # Represent graph as an adj matrix where G(u,v) = no. of undirected edges from node U to node V
    ''' 
    :param filename: the filename formatted where 
                        the first line contains N, the number of nodes in the graph
                        followed by an arbitrary number of space-separated pairs 'A B', 
                        which represent an edge in the graph from nodes A to nodes B.
    Constructor for the graph. Builds a graph (adj matrix representation) from the data 
    in the input file.
    '''
    def __init__(self, filename='data.txt'):
        data_file = open(filename, 'r')

        # the number of nodes in this graph
        self.n = int(data_file.readline())

        # initialize an NxN adjacency matrix for our graph
        self.graph = np.zeros((self.n, self.n))

        # stores the (i, j) coordinates of all the valid edges in the adj matrix
        # note: only stores the edges in the upper-right triangular matrix (since the matrix is symmetric)
        self.edge_list = []

        # read in the edges from the file
        for line in data_file:
            nodes = list(map(int, line.split())) # splits the string on whitespace
            
            self.graph[nodes[0]][nodes[1]] += 1
            # we have an undirected graph, so edge A->B also means edge B->A
            self.graph[nodes[1]][nodes[0]] += 1

            # add this edge to our edge list, with the smaller node coming first
            if nodes[0] > nodes[1]:
                nodes[0], nodes[1] = nodes[1], nodes[0]
            self.edge_list.append([nodes[0], nodes[1]])

        data_file.close()

    '''
    prints the graph in adj matrix format
    '''
    def printGraph(self):
        print(self.graph)

    ''' 
    :param node_u: the first endpoint of the edge
    :param node_v: the second endpoint of the edge
    contracts the edge between node_u and node_v in graph
    ''' 
    def contract(self, node_u, node_v):
        # let node_u always be the smaller index
        if node_u > node_v:
            # swap them if node_u > node_v
            node_u, node_v = node_v, node_u

        # Add row u to row v
        for i in range(self.n):
            self.graph[node_v][i] += self.graph[node_u][i]

        # Add col u to col v
        for i in range(self.n):
            self.graph[i][node_v] += self.graph[i][node_u]

        # Zero out row u and col u (delete node u)
        self.graph[node_u] = 0
        self.graph[:, node_u] = 0

        new_edge_list = []
        # re attach the edges
        for edge in self.edge_list:
            if edge[0] == node_u:
                edge[0] = node_v
            elif edge[1] == node_u:
                edge[1] = node_v
            
            # dont keep self loops after the contraction
            if edge[0] != edge[1]:
                new_edge_list.append(edge)

        self.edge_list = new_edge_list

        # Set G(v, v) = 0 (removes self-loop on node v in adj matrix)
        self.graph[node_v][node_v] = 0


    '''
    randomly and uniformly selects an edge from graph
    returns i,j such that they form an edge in the graph
    '''
    def random_pick(self):
        edgePair = self.edge_list[np.random.choice(len(self.edge_list))]
        return edgePair[0], edgePair[1]

'''
:param graphObj: the graph object to do karger's on
utilizes karger's algorithm to find the min-cut of graph
Note: this is a Monte Carlo algorithm, meaning the returned cut is
not necessarily the min.
returns the number of edges in the min-cut found
'''
def kargers(graphObj):
    # make a copy of the graph to modify
    graphCopy = copy.deepcopy(graphObj)

    # keep going while there are more than 2 vertices in the graph
    # each iteration removes a vertex, so we will do n-2 iterations
    for i in range(graphCopy.n-2):
        # uniformly pick a random edge in the graph
        u, v = graphCopy.random_pick()

        # contract it
        graphCopy.contract(u, v)
    # min-cut is represented by the remaining 2 supernodes
    # we return the # of edges between them, as this is the size of the cut
    return graphCopy.graph.sum(axis=None) / 2

''' main function for Karger's Min-Cut application '''
if __name__ == '__main__':
    # For convinience, each of the N computers in the data file is labelled 0, 1, 2, ... N. 
    graphObj = Graph(filename='data_4_comps_10_networks.txt')
    
    # in the worst case, we remove all the edges
    min_cut = len(graphObj.edge_list)
    
    NUM_TRIALS = 100
    for i in range(NUM_TRIALS):
        # over multiple trials, take the minimum result we've seen
        min_cut = min(min_cut, kargers(graphObj))
    
    # prints the min number of edges that, if removed, will disconnect the graph
    print(min_cut)