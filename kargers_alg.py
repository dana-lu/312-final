# 312 Final Project - Karger's Min-Cut Algorithm

import numpy as np

# Represent graph as an adj matrix where G[u][v] = # of edges from node U to node V
# For simplicity, each of the computers is labelled 0, 1, 2, ... N. 

# This class represents a graph data structure with data intialized from a file
class Graph:
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
        n = data_file.readline()

        # initialize an NxN adjacency matrix for our graph
        self.graph = np.zeros((int(n), int(n)))

        # read in the edges from the file
        for line in data_file:
            nodes = line.split() # splits the string on whitespace
            
            self.graph[int(nodes[0])][int(nodes[1])] += 1
            # we have an undirected graph, so A->B implies B->A
            self.graph[int(nodes[1])][int(nodes[0])] += 1

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

''' main function for Karger's Min-Cut application '''
if __name__ == '__main__':
    graph = Graph(filename= 'data.txt')
    graph.printGraph()

    # keep going while there are 2 vertices in the graph
    while():
        pass

    # min-cut is represented by the remaining 2 supernodes
    print()

