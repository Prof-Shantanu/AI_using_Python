# checking if the color is available
def is_safe(graph, color, node, c):

    for i in graph[node]:
        if color[i] == c:
            return False
    return True

# assigning colors to the graph
def graph_coloring_util(graph, n_col, color, node):
    if node == len(graph):
        return True

    for c in range(1, n_col + 1):
        if is_safe(graph, color, node, c):
            color[node] = c
            # calling the function recursively for the next node
            if graph_coloring_util(graph, n_col, color, node + 1):
                return True
            color[node] = 0
    return False

def graph_coloring(graph, n_col):
    color = [0] * len(graph)
    if graph_coloring_util(graph, n_col, color, 0):
        return color
    else:
        return False

# Example usage:
graph = {0: [1, 2],
         1: [0, 2, 3],
         2: [0, 1, 3],
         3: [1, 2]}
m = 3# Maximum number of colors (could be set to 4 for the Four Color Theorem)

coloring = graph_coloring(graph, m)
if coloring:
    print("Coloring found:", coloring)
else:
    print("No valid coloring found")
