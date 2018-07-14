from .node import Node


class Graph(dict):

    def __init__(self, raw_dict=None):
        super().__init__()
        self.open_list = []
        self.closed_list = []
        for key, value in raw_dict.items():
            node_key = Node(key)
            self[node_key] = []
            for item in value:
                self[node_key].append(Node(item))
