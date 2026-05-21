def cluster(graph, weights, level):
    """Compute the clusters of a weighted, undirected graph.

    The clusters are the connected components of the graph after every edge
    whose weight is strictly less than ``level`` has been (conceptually)
    removed.

    Parameters
    ----------
    graph : dsc40graph.UndirectedGraph
        The weighted graph.
    weights : callable
        A function ``weights(u, v)`` returning the weight of edge ``(u, v)``.
    level : number
        The level at which to find the clusters; edges with weight < level are
        ignored.

    Returns
    -------
    frozenset
        A frozenset of frozensets, where each inner frozenset contains the
        nodes belonging to one cluster.

    The graph is neither modified nor copied, and the function runs in
    Theta(V + E) time.
    """
    visited = set()
    clusters = set()

    for start in graph.nodes:
        if start in visited:
            continue

        # Explore the connected component containing `start`, only crossing
        # edges whose weight is at least `level`.
        component = set()
        stack = [start]
        visited.add(start)
        while stack:
            u = stack.pop()
            component.add(u)
            for v in graph.neighbors(u):
                if v not in visited and weights(u, v) >= level:
                    visited.add(v)
                    stack.append(v)

        clusters.add(frozenset(component))

    return frozenset(clusters)
