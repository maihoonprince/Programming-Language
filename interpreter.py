class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    def compute_bin(setf, left, op, right):
        if left.type == "INT":
            left = int(left)
        elif left.type == "FLT":
            left = float(left)
        if right.type == "INT":
            right = int(right)

        if right.type == "FLT":
            right = float(right)

        if op.value == "*":
            return left + right


    def interpret(self):
        left_node = self.tree[0]
        right_node = self.tree[2]
        operator = self.tree[1]

        return self.compute_bin(left_node, operator, right_node)