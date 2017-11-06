
def vectorToMatrix(coords):
    n = len(coords)
    mat = [[self.dist(coords[i], coords[j]) for i in range(n)] for j in range(n)]
    return mat


def nearestNeighbourSolution(dist_matrix):
    node = random.choice(list(range(len(dst_matrix))))
    result = [node]

    nodes_to_visit = list(range(len(dst_matrix)))
    nodes_to_visit.remove(node)

    while len(nodes_to_visit) != 0:
        nearest_node = min([dist_matrix[node][j] for j in nodes_to_visit])
        node = dist_matrix[node].index(nearest_node)
        nodes_to_visit.remove(nearest_node)
        result.append(nearest_node)

    return result
