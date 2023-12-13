import networkx as nx
import scipy
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import reverse_cuthill_mckee
import numpy as np

def RCM(G):
    '''
    Reorder a graph according to reverse Cuthill-McKee heuristic
    
    parameters: G -> type: matrix
    
    return: RCM_A -> Adjacency matrix with reverse Cuthill-Mckee node reordering -> type: matrix
    '''

    if isinstance(G, np.ndarray):
        G = nx.from_numpy_array(G)
    # Convert sparse matrix to csr format & perform RCM reordering on nodes

    csr_G = nx.to_scipy_sparse_array(G)
    RCM_ordering = reverse_cuthill_mckee(csr_G)

    # If G is in csr format, convert to dense format, then calculate the adjacency matrix
    if type(G) == scipy.sparse._csr.csr_array:
        G = G.todense()
    A = nx.adjacency_matrix(G)

    # Reorder nodes according to RCM heuristic
    RCM_A = A[RCM_ordering, :][:, RCM_ordering]

    return RCM_A


