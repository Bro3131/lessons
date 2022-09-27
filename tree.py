class Tree:
    def __init__(self, data):
        # left child
        self.left = None
        # right child
        self.right = None
        # tree's value
        self.data = data

    def print_tree(self):
        print(self.data)


root = Tree(15)
root.print_tree()
