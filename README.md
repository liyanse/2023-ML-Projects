Dijkstra's algorithm is a graph search algorithm that solves the single-source shortest path problem for a graph with non-negative edge weights, producing a shortest path tree. This algorithm is often used in routing and as a subroutine in other graph algorithms. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later. The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

The algorithm works by maintaining a list of unvisited nodes and the distances between each node and the source node. Initially, the source node is the only node in the list and its distance is set to 0. The algorithm repeatedly selects the node with the smallest distance and expands it, updating the distances of its neighbors. Once all nodes have been visited, the algorithm has computed the shortest paths from the source node to all other nodes.

Dijkstra's algorithm can be used on both directed and undirected graphs. It is generally slower than breadth-first search, but more efficient than brute-force search.



