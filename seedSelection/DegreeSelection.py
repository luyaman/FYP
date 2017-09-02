from AbstractSelection import AbstractSelection


# Select nodes into seed set based in order of decreasing degree
class HighDegreeSelection(AbstractSelection):
    def __init__(self, graph, size):
        AbstractSelection.__init__(self, graph, size)

    def select(self):
        # total number of nodes in this graph
        nodes_num = self.graph.GetNodes()

        # list to store the degree of all nodes
        deg_count = []

        # calculate the degree of each nodes
        for node_id in range(nodes_num):
            node = self.graph.GetNI(node_id)
            deg_count.append(node.GetOutDeg())

        order = sorted(range(len(deg_count)), key=lambda index: deg_count[index])
        order.reverse()
        result = order[:self.size]
        return result
