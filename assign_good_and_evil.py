from collections import deque


def assign_good_and_evil(graph):
    """Attempt to 2-color the graph so every edge connects a 'good' node to an
    'evil' node. Returns a dict {node: 'good'|'evil'} if possible, else None.
    """
    labels = {}

    for start in graph.nodes:
        if start in labels:
            continue

        # BFS from this start node, alternating labels by BFS level.
        labels[start] = 'good'
        queue = deque([start])

        while queue:
            node = queue.popleft()
            opposite = 'evil' if labels[node] == 'good' else 'good'
            for neighbor in graph.neighbors(node):
                if neighbor not in labels:
                    labels[neighbor] = opposite
                    queue.append(neighbor)
                elif labels[neighbor] == labels[node]:
                    # Conflict: two adjacent nodes share a label -> not bipartite.
                    return None

    return labels
