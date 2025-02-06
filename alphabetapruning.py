class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        value = float('-inf') # INITIALIZING the value to negative inifinty.
        for child in node.children:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value) # UPDATE ALPHA value to be maximum of its current value and the new value.
            if beta <= alpha:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha pruning
        return value

# Example usage:
tree = Node(3, [
    Node(5, [
        Node(1),
        Node(2),
        Node(0)
    ]),
    Node(6, [
        Node(7),
        Node(8),
        Node(4)
    ]),
    Node(9, [
        Node(13),
        Node(11),
        Node(12)
    ])
])
result = alpha_beta(tree, depth=3, alpha=float('-inf'), beta=float('inf'), maximizing_player=True)
print("Result of the game tree evaluation:", result)
