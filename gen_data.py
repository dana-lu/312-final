# Generates the datasets for Karger's Min-Cut

'''
The text files are formatted as follows:
- The first line contains a single integer N, which represents the number of computers in the network. Each computer is numbered 
with an ID 0, 1, 2, ... N.
- Every line following the first line contains two single-spaced separated integers A B, which indicates that computer A
is connected to computer B in the network.
'''

import numpy as np

NUM_COMPUTERS = 4

NUM_NETWORKS = 10

file_contents = []
file_contents.append(NUM_COMPUTERS)

# first guarantee that the graph is connected
for i in range(1, NUM_COMPUTERS + 1):
    file_contents.append("{} {}".format(i-1, i % NUM_COMPUTERS))

for i in range(NUM_COMPUTERS + 1, NUM_NETWORKS + 1):
    edge = np.random.choice(NUM_COMPUTERS, size=2, replace=False)
    file_contents.append("{} {}".format(edge[0], edge[1]))

np.savetxt('data_{}_comps_{}_networks.txt'.format(NUM_COMPUTERS, NUM_NETWORKS), file_contents, fmt="%s")
