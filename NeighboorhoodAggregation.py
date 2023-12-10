import numpy as np
import scipy.sparse as sp
import random

def get_random_node_edges(csr_matrix):
    node_index = random.randint(0, csr_matrix.shape[0] - 1)

    # Find the indices of non-zero elements in the row
    row_start = csr_matrix.indptr[node_index]
    row_end = csr_matrix.indptr[node_index + 1]
    connected_nodes = csr_matrix.indices[row_start:row_end]

    return [(node_index, connected_node) for connected_node in connected_nodes]

def main():
    csr_matrix = sp.load_npz("/lustre/acslab/shared/Agatha_shared/2021_11_22/ensemble/adj_matrices_abstr_enrich/scipy_csr/aapp_aapp_edgelist.npz")

    for _ in range(1):
        get_random_node_edges(csr_matrix)

if __name__ == "__main__":
    main()
