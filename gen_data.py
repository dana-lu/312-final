# Generates the datasets for Karger's Min-Cut

'''
The text files are formatted as follows:
- The first line contains a single integer N, which represents the number of computers in the network. Each computer is numbered 
with an ID 0, 1, 2, ... N.
- Every line following the first line contains two single-spaced separated integers A B, which indicates that computer A
is connected to computer B in the network.
'''

import numpy as np

'''
:param num_computers: the number of computers desired in the network
:param num_networks: the number of networks desired in the network (must be >= num_computers)
'''
def gen_data(num_computers, num_networks):
    if num_computers > num_networks:
        print("NUM_NETOWRKS must >= NUM_COMPUTERS")

    else:
        file_contents = []
        file_contents.append(num_computers)

        # first guarantee that the graph is connected
        for i in range(1, num_computers + 1):
            file_contents.append("{} {}".format(i-1, i % num_computers))

        # add additional edges to get to NUM_NETWORKS
        for i in range(num_computers + 1, num_networks + 1):
            # use replace=false to prevent self-loops
            edge = np.random.choice(num_computers, size=2, replace=False)
            file_contents.append("{} {}".format(edge[0], edge[1]))

        np.savetxt('data_{}_comps_{}_networks.txt'.format(num_computers, num_networks), file_contents, fmt="%s")

if __name__ == '__main__':
    for i in range(1, 21):
        gen_data(i*10, i*20)

