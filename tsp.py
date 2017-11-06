from nodes_generator import NodeGenerator
from simulated_annealing import SimulatedAnnealing

def main():

    nodes = NodeGenerator(100, 100, 30).generate()

    temp = 6
    stopping_temp = 0.00000001
    alpha = 0.9995
    stopping_iter = 100000000

    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)

    sa.anneal()


if __name__ == "__main__": main()
