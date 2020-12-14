# Requirement
 Given an undirected graph with costs, find a Hamiltonian cycle of low cost (approximate TSP) by using the heuristic of sorting the edges in increasing order of their costs and, for each edge, choose it if and only if it does not close a cycle of length lower than n.
 
 I implemented my own undirected graph and the application also offers these operations:
 - read the graph from a file or generate a random one;
 - parse the set of vertices / the set of edges of a specified vertex;
 - add / remove an edge;
 - add / remove a vertex;
 - save the graph to a text file;
 - copy the graph;
 
 The application has a **layered architecture**.
