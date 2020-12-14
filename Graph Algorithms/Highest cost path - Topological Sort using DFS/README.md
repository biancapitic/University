# Requirement

Write a program that, given a graph with costs, does the following:
- verify if the corresponding graph is a DAG and performs a topological sorting of the activities using the algorithm based on **DFS** (Tarjan's algorithm);
- if it is a DAG, finds a highest cost path between two given vertices, in O(m+n).

The requirement is solved on my implementation of a directed graph.
The application implements offers also other operations:
- generate a random graph;
- add / remove an edge;
- add / remove a vertex;
- parse the set of vertices / the set of outbound vertices of a vertex / the set of inbound vertices of a vertex;
- check if there is an edge between 2 vertices;
- save the graph in a file;
The graph is read from a text file.
The entire application is implemented using a **layered architecture pattern**.
