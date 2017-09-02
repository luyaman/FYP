import abc


class AbstractSelection:
    __metaclass__ = abc.ABCMeta

    def __init__(self, graph, size):
        self.graph = graph
        self.size = size

    @abc.abstractmethod
    def select(self):
        """
        Select an optimal seed set of given size
        """
        return
