def biggest_descendent(graph, root, value):
    """Return a dictionary mapping each node to its biggest descendent value.

    The biggest descendent value of a node ``u`` is the largest value of any
    node that is a descendent of ``u`` in the tree (where ``u`` is considered a
    descendent of itself).

    Parameters
    ----------
    graph : dsc40graph.DirectedGraph
        A directed graph that is a tree, with edges pointing from parents to
        children.
    root : node
        The label of the root node of the tree.
    value : dict
        A dictionary mapping each node to its value.

    Returns
    -------
    dict
        A dictionary mapping each node to its biggest descendent value.

    Runs in Theta(V + E) time using a post-order depth-first search.
    """
    biggest = {}

    def visit(u):
        best = value[u]
        for child in graph.neighbors(u):
            best = max(best, visit(child))
        biggest[u] = best
        return best

    visit(root)
    return biggest
