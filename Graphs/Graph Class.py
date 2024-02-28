class Graph:
    def __init__(self, V: list, E: set[tuple]) -> None:
        """Declare attribues

        Source: https://www.youtube.com/watch?v=uFaZY1dVnGs&t=448s

        Args:
            V (set): Nodes in the Graph
            E (set of tuples): Edges in the form of tuples
        """
        #
        # since we already have the vertices as keys in the dictionary
        # we don't acutally need this. This approach is called  an adjacency
        # set or adjaceny mapping
        #
        # self.V = set(V)
        #
        # A set is required, an ordinary set cannot contain sets,
        # eg. {{1,2},{2,3}} will result in an error. frozenset()
        # allows for this.
        
        # On the other hand, all future calls fail using 
        # frozenset.
        # 
        self.E = set(frozenset((u,v) for u,v in E))
        self._neighbors = {}
        for v in V:
            self.add_vertex(v)
        for u,v in self.E:
            self.add_edge(u,v)

    def add_vertex(self, v):
        if v not in self._neighbors:
            self._neighbors[v] = set()
        
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
#        self.E.add(frozenset([u,v]))
        self.E.add((u,v))
        self._neighbors[u].add(v)
        self._neighbors[v].add(u)
        
    def remove_edge(self, u, v):
        # in the source the following was used but procduced a key error
        # self.E.remove(frozenset([u,v]))
        if (u,v) in self.E:
            self.E.remove((u,v))
            self._neighbors[u].remove(v)
            self._neighbors[v].remove(u)
            
    def remove_vertex(self, u):
        to_delete = list(self._neighbors[u])
        for v in to_delete:
            self.remove_edge(u,v)
            self.remove_edge(v,u)
        del self._neighbors[u]

    def deg(self, v):
        return len(self._neighbors[v])
    
    def neighbors(self, v):
        # by returning an iterator, the data set itself remains private
        # and cannot be altered
        return iter(self._neighbors[v])

    @property    
    def m(self):
        # This returns the number of edges. The name "m" is conventional.
        # It is declared as a property for convience in calling
        return len(self.E)
        
    @property
    def n(self):
        # The number of vertices, "n" by convention
        return len(self._neighbors)
    
if __name__ ==  '__main__':
    G = Graph([1,2,3], {(1,2), (2,3)})
    assert(G.deg(1) == 1)
    assert(G.deg(2) == 2)
    assert(G.deg(3) == 1)
    assert(set(G.neighbors(2)) == {1,3})
    assert(G.n == 3 and G.m == 2)

    # print(set(G.E))
    
    G.remove_edge(1,2)
    assert(G.n == 3 and G.m == 1)
    
    G.remove_edge(1,3)
    assert(G.n == 3 and G.m == 1)

    # print(set(G.E))

    G.add_edge(1,2)
    assert(G.n == 3 and G.m == 2)
    
    # print(set(G.E))    
    G.remove_vertex(2)
    assert(G.n == 2 and G.m == 0)

    # print(G.E)

    # print(list(G.neighbors(2)))
    
    print("Okay")