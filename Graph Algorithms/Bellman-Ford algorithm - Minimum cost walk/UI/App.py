from Entities.DirectedGraph import DirectedGraph
from Service.Service import Service
from Exceptions.MyExceptions import GraphExceptions

class UI:
    def __init__(self, service):
        self._commands = {"1": self.__ui_read_from_a_file, "2": self.__ui_create_random_graph,
                          "3": self.__ui_get_number_of_vertices,
                          "4": self.__ui_parse_set_of_vertices,
                          "5": self.__ui_is_edge,
                          "6":self.__ui_get_in_and_out_degree_of_vertex,
                          "7":self.__ui_iterate_over_outbound_edges, "8": self.__ui_iterate_over_inbound_edges,
                          "9":self.__ui_get_edge_cost, "10":self.__ui_change_edge_cost, "11":self.__ui_add_an_edge,
                          "12":self.__ui_remove_edge, "13":self.__ui_add_vertex, "14":self.__ui_remove_vertex,
                          "15":self.__ui_write_the_graph_in_a_textfile, "16":self.__ui_copy_graph,
                          "17": self.__ui_change_current_graph, "18":self.__ui_shortest_path,
                          "19":self.__ui__minimum_cost_path}
        self._service = service

    def __ui_read_from_a_file(self):
        filename = input("Enter filename for the graph: ")
        graph_name = input("Enter a name for the graph: ")
        try:
            self._service.read_graph_from_file(filename, graph_name)
        except FileNotFoundError:
            print("Name of file is wrong! Try again.")
        except GraphExceptions as e:
            print(e)

    def __ui_create_random_graph(self):
        try:
            vertices_number = int(input("Enter the number of vertices: "))
            edges_number = int(input("Enter the number of edges: "))
            graph_name = input("Enter a name for the graph: ")
            self._service.create_random_graph(vertices_number, edges_number, graph_name)
        except ValueError:
            print("Wrong input!")
        except GraphExceptions as e:
            print(e)

    def __ui_write_the_graph_in_a_textfile(self):
        filename = input("Enter filename: ")
        try:
            self._service.write_graph_to_file(filename)
        except FileNotFoundError:
            print("Name of file is wrong! Try again.")

    def __ui_get_number_of_vertices(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            print("The number of vertices is: ",  vertices_number)

    def __ui_parse_set_of_vertices(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            print("The vertices are: ")
            for vertex in self._service.service_get_iterable_of_vertices():
                print(vertex)

    def __ui_is_edge(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter source vertex: "))
                destination_vertex = int(input("Enter destination vertex: "))
                if self._service.service_check_if_edge_exists(source_vertex, destination_vertex) is True:
                    print("There is an edge from vertex ", source_vertex, " to vertex ", destination_vertex)
                else:
                    print("There is NO edge from vertex ", source_vertex, " to vertex ", destination_vertex)
            except GraphExceptions as e:
                print (e)
            except ValueError:
                print("Wrong input!")

    def __ui_get_in_and_out_degree_of_vertex(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                vertex = int(input("Enter the vertex: "))
                result = self._service.get_in_and_out_degree_of_vertex(vertex)
                print("The in degree of vertex ", vertex, "is: ", result[0])
                print("The out degree of vertex ", vertex, "is: ", result[1])
            except ValueError:
                print("Invalid input!")
            except GraphExceptions as e:
                print(e)

    def __ui_iterate_over_outbound_edges(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                vertex = int(input("Enter the vertex: "))
                print("The outbound edges of vertex ", vertex, " are: ")
                empty = True
                for destination_vertex in self._service.service_get_iterable_of_outbound_edges(vertex):
                    print("Edge: ", vertex, " -> ", destination_vertex)
                    empty = False
                if empty:
                    print("The vertex has no outbound edges.")
            except ValueError:
                print("Invalid input!")
            except GraphExceptions as e:
                print(e)

    def __ui_iterate_over_inbound_edges(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                vertex = int(input("Enter the vertex: "))
                print("The inbound edges of vertex ", vertex, " are: ")
                empty = True
                for source_vertex in self._service.service_get_iterable_of_inbound_edges(vertex):
                    print("Edge: ", source_vertex, " -> ", vertex)
                    empty = False
                if empty:
                    print("The vertex has no inbound edges.")
            except ValueError:
                print("Invalid input!")
            except GraphExceptions as e:
                print(e)

    def __ui_get_edge_cost(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter source vertex: "))
                destination_vertex = int(input("Enter destination vertex: "))
                cost = self._service.service_get_edge_cost(source_vertex, destination_vertex)
                print("The integer attached (the cost) to the edge ", source_vertex, " -> ", destination_vertex, " is: ", cost)
            except GraphExceptions as e:
                print (e)
            except ValueError:
                print("Wrong input!")

    def __ui_change_edge_cost(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter source vertex: "))
                destination_vertex = int(input("Enter destination vertex: "))
                cost = int(input("Enter new integer for the specified edge: "))
                self._service.service_change_edge_cost(source_vertex, destination_vertex, cost)
            except GraphExceptions as e:
                print (e)
            except ValueError:
                print("Wrong input!")

    def __ui_add_an_edge(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter source vertex: "))
                destination_vertex = int(input("Enter destination vertex: "))
                cost = int(input("Enter new integer for the specified edge: "))
                self._service.service_add_edge(source_vertex, destination_vertex, cost)
            except GraphExceptions as e:
                print(e)
            except ValueError:
                print("Wrong input!")

    def __ui_remove_edge(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter source vertex: "))
                destination_vertex = int(input("Enter destination vertex: "))
                self._service.service_remove_edge(source_vertex, destination_vertex)
            except GraphExceptions as e:
                print(e)
            except ValueError:
                print("Wrong input!")

    def __ui_remove_vertex(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                vertex = int(input("Enter vertex: "))
                self._service.service_remove_vertex(vertex)
            except GraphExceptions as e:
                print(e)
            except ValueError:
                print("Wrong input!")

    def __ui_add_vertex(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                vertex = int(input("Enter vertex: "))
                self._service.service_add_vertex(vertex)
            except GraphExceptions as e:
                print(e)
            except ValueError:
                print("Wrong input!")
    def __ui_copy_graph(self):
        graph_name = input("Enter a name for the graph: ")
        copy_of_the_graph = self._service.copy_graph(graph_name)
        print("The copy was made.")
        print("Below is the list of the graphs vertices so you can see that it's an accurate copy of the original graph.")
        for vertex in copy_of_the_graph.get_iterable_of_vertices():
            print(vertex)

    def __ui_change_current_graph(self):
        graphs_names_list = self._service.get_graphs_name_list()
        print("The names of the existing graphs are: ")
        for name in graphs_names_list:
            print(name)
        graph_name = input("Enter the name of the graph that you want to use: ")
        try:
            self._service.change_the_current_graph(graph_name)
            print("Current graph is the ", graph_name, " graph.")
        except GraphExceptions as e:
            print(e)

    def __ui_shortest_path(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter source vertex: "))
                destination_vertex = int(input("Enter destination vertex: "))
                path = self._service.service_get_shortest_path_between_start_end_vertices(source_vertex, destination_vertex)
                if len(path) != 1:
                    print("The shortest path has length: " + str(len(path) - 1))
                    print("The path is:")
                    index = 0
                    while index < len(path) - 1:
                        print(path[index], "-> ", end='')
                        index += 1
                    print(path[index])
                else:
                    print("The shortest path has length: 1")
                    print("The path is:")
                    print(path[0], "-> ", path[0])
            except GraphExceptions as e:
                print(e)
            except ValueError:
                print("Wrong input!")

    def __ui__minimum_cost_path(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter source vertex: "))
                destination_vertex = int(input("Enter destination vertex: "))
                path_cost = 0
                reversed_path = []
                path_cost, reversed_path = self._service.service_get_minimum_cost_path(source_vertex, destination_vertex)
                if path_cost is None and reversed_path == []:
                    print("We cannot find a minimum cost path between ", source_vertex,  " and ", destination_vertex,
                          "because there is a negative cost cycle accessible from the source vertex.\n")
                elif not reversed_path:
                    print("There is no path from ", source_vertex,  " to ", destination_vertex)
                elif len(reversed_path) == 1:
                    print("The minimum cost path between ", source_vertex,  " and ", destination_vertex, " is 0.\n")
                else:
                    print("The cost of the path is: ", path_cost)
                    i = len(reversed_path) - 1
                    print("The path is:")
                    while i > 0:
                        print(reversed_path[i], "-> ", end='')
                        i -= 1
                    print(reversed_path[0])
            except GraphExceptions as e:
                print(e)
            except ValueError:
                print("Wrong input!")

    def print_commands(self):
        print("\n"
              "0: Stop app!\n"
              "1: Read the graph from a file.\n"
              "2: Generate a random graph.\n"
              "3: Show number of vertices.\n"
              "4: Parse the set of vertices.\n"
              "5: Check if there is an edge between two vertices.\n"
              "6: Get the in degree and the out degree of a vertex.\n"
              "7: Parse the set of outbound edges of a specified vertex.\n"
              "8: Parse the set of inbound edges of a specified vertex.\n"
              "9: Retrieve the information (the integer) attached to a specified edge.\n"
              "10: Change the information (the integer) attached to a specified edge.\n"
              "11: Add a new edge.\n"
              "12: Remove an edge.\n"
              "13: Add a new vertex.\n"
              "14: Remove a vertex.\n"
              "15: Write the graph in a file.\n"
              "16: Copy the graph.\n"
              "17: Change the graph that you are now doing operations on.\n"
              "18: Find shortest path between two given vertices.\n"
              "19: Get minimum cost path between two vertices.")

    def run_app(self):
        while True:
            self.print_commands()
            command = input("Enter command: ")
            if command == "0":
                break
            elif command not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                                 "11", "12", "13", "14", "15", "16", "17", "18", "19"]:
                print("Wrong command!")
            else:
                self._commands[command]()
