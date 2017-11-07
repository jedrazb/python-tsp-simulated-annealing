import math
import random
import numpy as np

def vectorToMatrix(coords):
    n = len(coords)
    mat = [[dist(coords[i], coords[j]) for i in range(n)] for j in range(n)]
    return mat


def nearestNeighbourSolution(dist_matrix):
    node = random.randrange(len(dist_matrix))
    result = [node]

    nodes_to_visit = list(range(len(dist_matrix)))
    nodes_to_visit.remove(node)

    while nodes_to_visit:
        nearest_node = min([(dist_matrix[node][j], j) for j in nodes_to_visit], key=lambda x: x[0])
        node = nearest_node[1]
        nodes_to_visit.remove(node)
        result.append(node)

    return result

def dist(coord1, coord2):
    return np.linalg.norm(coord1 - coord2)
