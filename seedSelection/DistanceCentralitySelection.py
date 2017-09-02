from AbstractSelection import AbstractSelection
import snap


class DistanceCentralitySelection(AbstractSelection):
    def __init__(self, graph, size):
        AbstractSelection.__init__(self, graph, size)

    def calculate_average_distance(self, node_id):
        # build a hash table
        graph_hash = snap.TIntH()

        # calculate shortest path from given node to all other nodes
        snap.GetShortPath(self.graph, node_id, graph_hash)

        distance_acc = 0

        for node in graph_hash:
            distance_acc += graph_hash[node]

        return distance_acc/(len(graph_hash) - 1)

    def select(self):
        node_num = self.graph.GetNodes()

        # calculate the average distance of one node to all other reachable nodes
        average_distance = []
        for node_id in range(node_num):
            average_distance.append(self.calculate_average_distance(node_id))

        order = sorted(range(len(average_distance)), key=lambda index: average_distance[index])
        result = order[:self.size]
        return result
