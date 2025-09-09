import networkx as nx

def create_graph():
    """
    Cria e retorna o grafo que representa a cidade para otimização de entregas.
    """
    G = nx.Graph()
    G.add_node(0, name="HUB - Sabor Express")
    G.add_node(1, name="Centro (Area 1)")
    G.add_node(2, name="Bairro A")
    G.add_node(3, name="Bairro B")
    G.add_node(4, name="Cliente P1")
    G.add_node(5, name="Cliente P2")
    G.add_node(6, name="Cliente P3")
    G.add_node(7, name="Shopping")
    G.add_node(8, name="Cliente P4")
    G.add_node(9, name="Rua das Flores")
    G.add_node(10, name="Cliente P5")
    G.add_node(11, name="Cliente P6")
    G.add_node(12, name="Cliente P7")
    G.add_node(13, name="Cliente P8")
    G.add_node(14, name="Cliente P9")

    edges = [
        (0, 1, {'weight': 5}), (0, 2, {'weight': 8}), (0, 7, {'weight': 10}), (0, 9, {'weight': 12}),
        (1, 4, {'weight': 2}), (1, 2, {'weight': 3}), (1, 7, {'weight': 7}),
        (2, 3, {'weight': 4}), (2, 5, {'weight': 3}),
        (3, 6, {'weight': 2}),
        (7, 8, {'weight': 2}), (7, 13, {'weight': 3}), (7, 14, {'weight': 3}),
        (9, 10, {'weight': 2}), (9, 11, {'weight': 3}), (9, 12, {'weight': 2}),
        (5, 6, {'weight': 3}), (10, 11, {'weight': 1}), (11, 12, {'weight': 1}), (13, 14, {'weight': 1})
    ]
    G.add_edges_from(edges)
    return G

def find_shortest_path(graph, start_node, end_node):
    """
    Encontra o menor caminho entre dois nós em um grafo.
    """
    try:
        path = nx.dijkstra_path(graph, source=start_node, target=end_node, weight='weight')
        total_time = nx.dijkstra_path_length(graph, source=start_node, target=end_node, weight='weight')
        return path, total_time
    except nx.NetworkXNoPath:
        return None, None