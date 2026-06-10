"""Single linkage clustering via Kruskal's algorithm. DSC 40B - Super Homework."""


# --- Disjoint Set Forest (from course gist) ---------------------------------

class DisjointSetForest:

    def __init__(self, elements):
        self._core = _DisjointSetForestCore()

        self.element_to_id = {}
        self.id_to_element = {}

        for element in elements:
            eid = self._core.make_set()
            self.element_to_id[element] = eid
            self.id_to_element[eid] = element

    def find_set(self, element):
        """Finds the "representative" of the set containing the element."""
        return self.id_to_element[
            self._core.find_set(
                self.element_to_id[element]
            )
        ]

    def union(self, x, y):
        """Unions the set containing `x` with the set containing `y`."""
        x_id = self.element_to_id[x]
        y_id = self.element_to_id[y]
        self._core.union(x_id, y_id)

    def in_same_set(self, x, y):
        """Determines if elements x and y are in the same set."""
        return self.find_set(x) == self.find_set(y)


class _DisjointSetForestCore:

    def __init__(self):
        self._parent = []
        self._rank = []
        self._size_of_set = []

    def make_set(self):
        # get the new element's "id"
        x = len(self._parent)
        self._parent.append(None)
        self._rank.append(0)
        self._size_of_set.append(1)
        return x

    def find_set(self, x):
        try:
            parent = self._parent[x]
        except IndexError:
            raise ValueError(f'{x} is not in the collection.')

        if self._parent[x] is None:
            return x
        else:
            root = self.find_set(self._parent[x])
            self._parent[x] = root
            return root

    def union(self, x, y):
        x_rep = self.find_set(x)
        y_rep = self.find_set(y)

        if x_rep == y_rep:
            return

        if self._rank[x_rep] > self._rank[y_rep]:
            self._parent[y_rep] = x_rep
            self._size_of_set[x_rep] += self._size_of_set[y_rep]
        else:
            self._parent[x_rep] = y_rep
            self._size_of_set[y_rep] += self._size_of_set[x_rep]
            if self._rank[x_rep] == self._rank[y_rep]:
                self._rank[y_rep] += 1


# --- Single linkage clustering ----------------------------------------------

def slc(graph, d, k):
    """Single linkage clustering using Kruskal's algorithm.

    Parameters
    ----------
    graph : dsc40graph.UndirectedGraph
    d : callable
        d(edge) -> distance, where edge is a tuple of two nodes.
    k : int
        Number of clusters to find.

    Returns
    -------
    frozenset of k frozensets, each a cluster of nodes.
    """
    dsf = DisjointSetForest(graph.nodes)
    n_clusters = len(graph.nodes)

    # Kruskal's: process edges in increasing order of distance, merging
    # components; stop early once only k components remain.
    for edge in sorted(graph.edges, key=d):
        if n_clusters <= k:
            break
        u, v = edge
        if not dsf.in_same_set(u, v):
            dsf.union(u, v)
            n_clusters -= 1

    clusters = {}
    for node in graph.nodes:
        clusters.setdefault(dsf.find_set(node), set()).add(node)

    return frozenset(frozenset(cluster) for cluster in clusters.values())
