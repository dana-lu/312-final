# 312-final

To generate a custom dataset with a specified number of computers and networks, modify the constants `NUM_COMPUTERS` and `NUM_NETWORKS`. Note that `NUM_NETWORKS` must be at least `NUM_COMPUTERS`. The graph will first assign networks to the computer such that the computers form a connected network. If there are still networks remaining, they will be randomly generated. Note that some computers may have multiple networks between them. The resulting data will be in a formatted file named `data_<# computers>_comps_<# networks>_networks.txt`

To run Karger's, pass the data text file to the program and it will print out the size of the min cut.