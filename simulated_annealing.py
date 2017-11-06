import math
import random
import matplotlib as plt
import tsp_utils

class SimulatedAnnealing():
    def __init__(self, coords, temp, alpha, stopping_temp, stopping_iter):
        self.coords = coords
        self.sample_size = len(coords)
        self.temp = temp
        self.alpha = alpha
        self.stopping_temperature = stopping_temp
        self.stopping_iter = stopping_iter
        self.iteration = 1

        self.dist_matrix = tsp_utils.vectorToMatrix(coords)
        self.curr_solution = tsp_utils.nearestNeighbourSolution(self.dist_matrix)

        self.curr_weight = self.weight(self.curr_solution)
        self.initial_weight = self.curr_weight
        self.min_weight = self.curr_weight
        print(self.curr_weight)


    def weight(self, sol):
         return round(sum( [ self.dist_matrix[sol[i-1]][sol[i]] for i in range(1,self.sample_size) ] ) + self.dist_matrix[sol[0]][sol[self.sample_size-1]], 4)
