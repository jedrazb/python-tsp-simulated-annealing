import random

class NodeGenerator:
    def __init__(self, width, height, nodesNumber):
        self.width = width
        self.height = height
        self.nodesNumber = nodesNumber

    def generate(self):

        coords = list()

        for i in range(self.nodesNumber):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)

            coords.append((x, y))

        print(coords)
        return coords
