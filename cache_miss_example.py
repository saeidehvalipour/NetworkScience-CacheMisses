# cache_miss_example_revised.py
import random
import networkx as nx 
import cProfile


def create_large_list(size):
    # Creating a smaller list
    return [random.randint(0, 1000) for _ in range(size)]

def access_pattern(lst, size):
    # Accessing the list in a random non-sequential manner
    for _ in range(size):
        index = random.randint(0, len(lst) - 1)
        lst[index] += 1

def main():
    size = 10**3  # 1 million elements, reduced from 10 million
    large_list = create_large_list(size)

    # Access the list in a pattern likely to cause cache misses
    access_pattern(large_list, size)


def get_neighbors(adjacency_matrix, node):
    """
    
    Get the first-order neighbors of a given node in an adjacency matrix.
    
    Parameters:
    - adjacency_matrix (matrix)
    - node
    
    Returns:
    - list: List of all first order neighbors of the node.
    """

    if node < 0 or node >= adjacency_matrix.shape[0]:
        raise ValueError("Invalid Node")
    
    row = adjacency_matrix.getrow(node)
    neighbors = row.indices.tolist()

    return neighbors

G = nx.gnp_random_graph(1000, .01)
A = nx.adjacency_matrix(G)



if __name__ == "__main__":
    for i in range(A.shape[0]):
        if get_neighbors(A, i) and get_neighbors(A, i)!= [0]:
            get_neighbors(A, i)
