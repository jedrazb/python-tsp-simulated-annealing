import math
import random
import matplotlib as plt
import tsp_utils

class SimulatedAnnealing():
    def __init__(self, coords, temp, alpha, stopping_temp, stopping_iter):
        self.coords = coords
        self.n = len(coords)
        self.temp = temp
        self.alpha = alpha
        self.stopping_temperature = stopping_temp
        self.stopping_iter = stopping_iter
        self.iteration = 1

        self.dist_matrix = tsp_utils.vectorToMatrix(coords)
        self.curr_solution = tsp_utils.nearestNeighbourSolution(self.dist_matrix)
