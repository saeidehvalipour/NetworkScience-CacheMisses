import time
from RCM import RCM
from Fiedler import Fiedler
import scipy.io as sio
import os
import scipy.sparse as ss
import random

G_10k = ss.load_npz("/lustre/acslab/users/3281/NSFinalProject/Nathan/data/new_100k_csr.npz")
node_indices = list(range(G_10k.shape[0]))

def get_neighbors_of_neighbors(matrix, node):
    
    for i in range(G_10k.getnnz()):
        first_degree_neighbors = list(G_10k[i].nonzero()[1])
        for neighbor in first_degree_neighbors:
            second_degree_neighbors = G_10k[neighbor].nonzero()[1]

def main():
    random_node = random.shuffle(node_indices)
    for _ in range(100):
        get_neighbors_of_neighbors(G_10k, random_node)

if __name__ == "__main__":
    main()