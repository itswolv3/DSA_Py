from graph import Graph

my_graph = Graph()

my_graph.add_vertex("a")
my_graph.add_vertex("b")
my_graph.add_vertex("c")
my_graph.add_vertex("d")

my_graph.add_edge("a", "b")
my_graph.add_edge("a", "c")
my_graph.add_edge("a", "d")
my_graph.add_edge("b", "d")
my_graph.add_edge("c", "d")

my_graph.print_graph()
print("\n")
my_graph.remove_vertex("d")
my_graph.print_graph()

