import random
from datetime import datetime
from Queue import Queue


class ICDiffusion:
    def __init__(self, graph, seeds, prob, repeat=200):
        self.graph = graph
        self.seeds = seeds
        self.prop = prob
        self.repeat = repeat
        random.seed(datetime.now())

    # Calculate the outcome of one diffusion attempt with constant probability
    # Return: True (Success) or False (Failure)
    def cascade(self):
        return random.random() <= self.prop

    # Simulate the one entire diffusion process
    def simulate_diffusion(self):
        # total number of nodes in this graph
        nodes_num = self.graph.GetNodes()

        # initialize the array to represent active/inactive state of each node
        nodes_active = [(index in self.seeds) for index in range(nodes_num)]

        # initialize the queue to represent the set of newly activated nodes in step t
        new_active = Queue(nodes_num)
        for seed in self.seeds:
            new_active.put(seed)

        while not(new_active.qsize() == 0):
            new_active_node = self.graph.GetNI(new_active.get())
            for out_neighbor in new_active_node.GetOutEdges():
                if not(nodes_active[out_neighbor]) and self.cascade():
                    new_active.put(out_neighbor)
                    nodes_active[out_neighbor] = True
        # print(nodes_active.count(True))
        return nodes_active.count(True)

    # Calculate expected size of active set
    def cal_expected(self):
        acc = 0
        for _ in range(self.repeat):
            acc += self.simulate_diffusion()
        return acc/self.repeat
