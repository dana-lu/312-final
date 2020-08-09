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

        # W[i] is the sum of the values in the i-th row of the 
        # upper-right triangular adj matrix
        # tldr: W stores the edges for random & uniform edge selection
        self.W = self.n * [0]

        # read in the edges from the file
        for line in data_file:
            nodes = list(map(int, line.split())) # splits the string on whitespace
            
            self.graph[nodes[0]][nodes[1]] += 1
            # we have an undirected graph, so edge A->B also means edge B->A
            self.graph[nodes[1]][nodes[0]] += 1

        for i in range(self.n):
            for j in range(i+1, self.n):
                self.W[i] += self.graph[i][j]
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

        # Set G(u, v) = 0 (removes self-loop)
        self.graph[node_v][node_v] = 0

        # update W
        self.W[node_u] -= 1

    '''
    :param W: an array where W[i] is the sum of the values of the 
                i-th row in the upper-right triangle of the adj matrix.
    randomly and uniformly selects an edge from graph
    returns i,j such that they form an edge in the graph
    '''
    def random_pick(self):
        edge_list = []
        
        # put all the valid edges into a list
        for i in range(self.n):
            for j in range(i+1, self.n):
                if(self.graph[i][j] != 0):
                    # if there are multiple edges from node A to node B, add that many elements to the list
                    for k in range(int(self.graph[i][j])):
                        edge_list.append((i, j))
        # randomly select an index in the list; the edge at that index will be the randomly selected one
        edgePair = edge_list[np.random.choice(len(edge_list))]
        
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
    graphObj = Graph(filename='data.txt')
    print(kargers(graphObj))