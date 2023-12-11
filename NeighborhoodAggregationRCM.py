import scipy.sparse as sp
from scipy.sparse.csgraph import reverse_cuthill_mckee
import numpy as np
import random

def load_csr_matrix(file_path):
    return sp.load_npz(file_path)

def get_random_node_neighbors(csr_matrix):

    random_node = random.choice(range(csr_matrix.shape[0]))
    neighbors = csr_matrix[random_node].nonzero()[1].tolist()
    return random_node, neighbors

def apply_rcm(csr_matrix):
    reverse_subgraph = reverse_cuthill_mckee(csr_matrix)
    rcm_matrix = csr_matrix[reverse_subgraph, :][:, reverse_subgraph]
    return rcm_matrix

def main():
    file_path = "/lustre/acslab/shared/Agatha_shared/2021_11_22/ensemble/adj_matrices_abstr_enrich/scipy_csr/aapp_aapp_edgelist.npz"

    csr_matrix = load_csr_matrix(file_path)
    rcm_matrix = apply_rcm(csr_matrix)

    for _ in range(1):
        random_node, neighbors = get_random_node_neighbors(rcm_matrix)

if __name__ == "__main__":
    main()



