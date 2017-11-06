import math
import random

def vectorToMatrix(coords):
    n = len(coords)
    mat = [[dist(coords[i], coords[j]) for i in range(n)] for j in range(n)]
    return mat


def nearestNeighbourSolution(dist_matrix):
    node = random.choice(list(range(len(dist_matrix))))
    result = [node]

    nodes_to_visit = list(range(len(dist_matrix)))
    nodes_to_visit.remove(node)

    while nodes_to_visit:
        nearest_node = min([dist_matrix[node][j] for j in nodes_to_visit])
        node = dist_matrix[node].index(nearest_node)
        nodes_to_visit.remove(node)
        result.append(node)

    return result


def dist(coord1, coord2):
    return round( math.sqrt( math.pow(coord1[0] - coord2[0], 2) + math.pow(coord1[1] - coord2[1], 2)  ), 4)
