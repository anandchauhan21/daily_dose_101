"""
There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:

Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.


Example 1:


Input
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
Output
[null, 6, -1, null, 6]

Explanation
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.


Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1)
edges[i].length == edge.length == 3
0 <= fromi, toi, from, to, node1, node2 <= n - 1
1 <= edgeCosti, edgeCost <= 106
There are no repeated edges and no self-loops in the graph at any point.
At most 100 calls will be made for addEdge.
At most 100 calls will be made for shortestPath.
"""


class Graph:
    def __init__(self, n: int, edges: List[Tuple[int, int, int]]):
        # Initialize the graph with a defaultdict where each node maps to a list of (neighbor, edge_cost) tuples
        self.graph = defaultdict(list)
        for from_node, to_node, edge_cost in edges:
            self.graph[from_node].append((to_node, edge_cost))

    def addEdge(self, edge: Tuple[int, int, int]) -> None:
        # Add a new edge to the graph
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, start_node: int, end_node: int) -> int:
        # Initialize minimum costs for each node with infinity, set the starting node cost to 0
        min_costs = defaultdict(lambda: float('inf'))
        min_costs[start_node] = 0

        # Initialize the priority queue with a tuple (cost, node)
        heap = [(0, start_node)]

        while heap:
            # Pop the node with the minimum cost from the priority queue
            cur_cost, cur_node = heapq.heappop(heap)

            # If the current node is the destination, return the minimum cost to reach it
            if cur_node == end_node:
                return min_costs[end_node]

            # Explore neighbors and update costs
            for nei, edge_cost in self.graph[cur_node]:
                new_cost = cur_cost + edge_cost
                # If the new cost is smaller than the current recorded cost for the neighbor, update it
                if new_cost < min_costs[nei]:
                    min_costs[nei] = new_cost
                    # Add the neighbor and its new cost to the priority queue
                    heapq.heappush(heap, (new_cost, nei))

        # If there is no path from start_node to end_node
        return -1