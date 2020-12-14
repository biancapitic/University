import copy
import sys
from random import randrange

class DirectedGraph:
    def __init__(self, vertices_number):
        self._dictOut = {}
        self._dictIn = {}
        self._dictCosts = {}
        self._vertices_number = vertices_number
        self._edges_number = 0

    def initialize_dictionaries_of_the_graph(self, number_of_vertices):
        self._vertices_number = number_of_vertices
        for index in range(0, number_of_vertices):
            self._dictOut[index] = []
            self._dictIn[index] = []

    def add_vertex(self, new_vertex):
        self._dictIn[new_vertex] = []
        self._dictOut[new_vertex] = []
        self._vertices_number += 1

    def is_vertex(self, searched_vertex):
        for vertex in self._dictOut:
            if searched_vertex == vertex:
                return True
        return False

    def add_edge(self, source_vertex, destination_vertex, cost):
        cost_dictionary_key = (source_vertex, destination_vertex)
        self._dictOut[source_vertex].append(destination_vertex)
        self._dictIn[destination_vertex].append(source_vertex)
        self._dictCosts[cost_dictionary_key] = cost
        self._edges_number += 1

    def _get_position_of_vertex_in_list(self, vertex, vertices_list):
        vertex_index = 0
        while vertex_index < len(vertices_list):
            if vertices_list[vertex_index] == vertex:
                return vertex_index
            vertex_index += 1
        return -1

    def _remove_vertex_from_dIn(self, destination_vertex, vertex_to_remove):
        index_vertex_to_remove = self._get_position_of_vertex_in_list(vertex_to_remove, self._dictIn[destination_vertex])
        if index_vertex_to_remove == -1:
            return -1
        self._dictIn[destination_vertex].pop(index_vertex_to_remove)

    def _remove_vertex_from_dOut(self, source_vertex, vertex_to_remove):
        index_vertex_to_remove = self._get_position_of_vertex_in_list(vertex_to_remove, self._dictOut[source_vertex])
        if index_vertex_to_remove == -1:
            return -1
        self._dictOut[source_vertex].pop(index_vertex_to_remove)

    def remove_edge(self, source_vertex, destination_vertex):
        del self._dictCosts[source_vertex, destination_vertex]
        self._remove_vertex_from_dIn(destination_vertex, source_vertex)
        self._remove_vertex_from_dOut(source_vertex, destination_vertex)
        self._edges_number -= 1

    def remove_vertex(self, vertex):
        for destination_vertex in self._dictOut[vertex]:
            self._remove_vertex_from_dIn(destination_vertex, vertex)
            del self._dictCosts[(vertex, destination_vertex)]
            self._edges_number -= 1
        for source_vertex in self._dictIn[vertex]:
            self._remove_vertex_from_dOut(source_vertex, vertex)
            del self._dictCosts[(source_vertex, vertex)]
            self._edges_number -= 1
        del self._dictIn[vertex]
        del self._dictOut[vertex]
        self._vertices_number -= 1

    def get_number_of_vertices(self):
        return self._vertices_number

    def get_iterable_of_vertices(self):
        for vertex in list(self._dictOut.keys()):
            yield vertex

    def get_in_degree(self, vertex):
        return len(self._dictIn[vertex])

    def get_out_degree(self, vertex):
        return len(self._dictOut[vertex])

    def is_edge(self, source_vertex, destination_vertex):
        for vertex in self._dictOut[source_vertex]:
            if destination_vertex == vertex:
                return True
        return False

    def get_iterable_of_outbound_edges(self, vertex):
        for destination_vertex in self._dictOut[vertex]:
            yield destination_vertex

    def get_iterable_of_inbound_edges(self, vertex):
        for source_vertex in self._dictIn[vertex]:
            yield source_vertex

    def get_edge_cost(self, source_vertex, destination_vertex):
        return self._dictCosts[(source_vertex, destination_vertex)]

    def change_edge_cost(self, source_vertex, destination_vertex, new_cost):
        self._dictCosts[(source_vertex, destination_vertex)] = new_cost

    def get_copy_of_graph(self):
        new_graph = copy.deepcopy(self)
        return new_graph

    def get_number_of_edges(self):
        return self._edges_number

    def create_random_edge(self):
        valid = False
        while not valid:
            start_vertex = randrange(0, self._vertices_number)
            end_vertex = randrange(0, self._vertices_number)
            cost = randrange(-10000, 10000)
            if start_vertex != end_vertex and not self.is_edge(start_vertex, end_vertex):
                valid = True
                self.add_edge(start_vertex, end_vertex, cost)

    def get_graph_in_format_for_textfile(self):
        lines = [str(self.get_number_of_vertices()) + " " + str(self.get_number_of_edges())]
        for edge in self._dictCosts:
            lines.append(str(edge[0]) + " " + str(edge[1]) + " " + str(self._dictCosts[edge]))
        for vertex in self._dictOut:
            if len(self._dictOut[vertex]) == 0 and len(self._dictIn[vertex]) == 0:
                lines.append(str(vertex) + " -1")
        return lines

    def get_shortest_path_between_start_end_vertices(self, start_vertex, end_vertex):
        queue = []
        visited = {}

        # initialize visited dictionary
        for vertex in self._dictOut.keys():
            visited[vertex] = -1

        queue.append(end_vertex)
        visited[end_vertex] = -2
        found = False
        while len(queue) > 0 and not found:
            vertex = queue.pop(0)
            for prev_vertex in self._dictIn[vertex]:
                if visited[prev_vertex] == -1 or visited[prev_vertex] == -2:
                    queue.append(prev_vertex)
                    visited[prev_vertex] = vertex
                    if prev_vertex == start_vertex:
                        found = True
                        break

        # this means that there is no path from start_vertex to end_vertex
        if visited[start_vertex] == -1 or visited[start_vertex] == -2:
            return []

        path = []
        vertex = start_vertex
        if start_vertex == end_vertex:
            path.append(vertex)
            vertex = visited[vertex]

        while vertex != end_vertex:
            path.append(vertex)
            vertex = visited[vertex]
        path.append(end_vertex)
        return path

    def get_minimum_cost_path(self, source_vertex, destination_vertex):
        distance = {}
        predecessor = {}

        if source_vertex == destination_vertex:
            return 0, [source_vertex]

        # initialize the distance and predecessor dictionaries
        for vertex in self._dictIn:
            if vertex == source_vertex:
                distance[vertex] = 0
            else:
                distance[vertex] = sys.maxsize
            predecessor[vertex] = -1

        # relax edges
        changed = True
        iteration = 1
        while changed and iteration < self._vertices_number:
            changed = False
            for edge in self._dictCosts.keys():
                if distance[edge[1]] > distance[edge[0]] + self._dictCosts[edge]:
                    distance[edge[1]] = distance[edge[0]] + self._dictCosts[edge]
                    predecessor[edge[1]] = edge[0]
                    changed = True
            iteration += 1

        # check for negative cost cycle
        # if the iteration number is smaller than vertices_number then there can't be a negative cost cycle
        # so we won't check for it
        # otherwise we will do one more iteration over the edges and if we have a change than it means that there is a
        # negative cost cycle
        if iteration == self._vertices_number:
            changed = False
            for edge in self._dictCosts.keys():
                if distance[edge[1]] > distance[edge[0]] + self._dictCosts[edge]:
                    distance[edge[1]] = distance[edge[0]] + self._dictCosts[edge]
                    predecessor[edge[1]] = edge[0]
                    changed = True
            if changed is True:
                return None, []

        # if there is no path between source_vertex and end_vertex
        if distance[destination_vertex] == sys.maxsize:
            return 0, []

        # we construct the minimum cost reversed_path from source_vertex to destination_vertex
        reversed_path = []
        vertex = destination_vertex
        reversed_path.append(destination_vertex)
        while vertex != source_vertex:
            reversed_path.append(predecessor[vertex])
            vertex = predecessor[vertex]

        return distance[destination_vertex], reversed_path