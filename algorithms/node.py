

class Node:

    def __init__(self, number):
        self.number = number
        self.H = None
        self.G = None
        self.F = None

    def __repr__(self):
        return str(self.number)
