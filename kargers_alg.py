# 312 Final Project - Karger's Min-Cut Algorithm

import numpy as np

'''
This class represents a graph data structure with data intialized from a file
'''
class Graph:
    # Represent graph as an adj matrix where G[u][v] = no. of undirected edges from node U to node V
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
        n = int(data_file.readline())

        # initialize an NxN adjacency matrix for our graph
        self.graph = np.zeros((n, n))

        # read in the edges from the file
        for line in data_file:
            nodes = list(map(int, line.split())) # splits the string on whitespace
            
            self.graph[nodes[0]][nodes[1]] += 1
            # we have an undirected graph, so A->B implies B->A
            self.graph[nodes[1]][nodes[0]] += 1

        data_file.close()

    '''
    prints the graph
    '''
    def printGraph(self):
        print(self.graph)


''' 
:param graph: the graph to do a contraction on
:param nodeA: the first endpoint of the edge
:param nodeB: the second endpoint of the edge
contracts the edge between nodeA and nodeB in graph
''' 
def contract(graph, nodeA, nodeB):
    pass   

'''
:param graph: the graph to randomly pick an edge from
:param W: an array where W[i] is the sum of the values of the 
            i-th row in the upper-right triangle of the adj matrix.
randomly and uniformly selects an edge from graph
'''
def random_pick(graph, W):
    pass

'''
:param graph: the graph to find the min-cut of
utilizes karger's algorithm to find the min-cut of graph
Note: this is a Monte Carlo algorithm, meaning the returned cut is
not necessarily the min.
'''
def kargers(graph):
    # keep going while there are more than 2 vertices in the graph
    while():
        pass

    # min-cut is represented by the remaining 2 supernodes
    print()

''' main function for Karger's Min-Cut application '''
if __name__ == '__main__':
    # For convinience, each of the N computers in the data file is labelled 0, 1, 2, ... N. 
    graph = Graph(filename= 'data.txt')
    graph.printGraph()

