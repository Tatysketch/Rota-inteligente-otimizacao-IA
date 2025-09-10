import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from src.graph import create_graph, find_shortest_path
from src.clustering import perform_clustering

# Simulação de um dataset de cidades para o grafo
cities = {
    'A': (30, 10), 'B': (20, 15), 'C': (25, 35), 'D': (10, 25), 
    'E': (40, 10), 'F': (45, 15), 'G': (42, 30), 'H': (5, 20),
    'I': (12, 28), 'J': (28, 5)
}

# --- Execução principal do fluxo ---
if __name__ == '__main__':
    # 1. Agrupamento de Clientes
    df_customers, kmeans = perform_clustering()
    n_clusters = kmeans.n_clusters
    
    # 2. Criação do Grafo da Cidade
    city_graph = create_graph(cities)
    
    # 3. Análise de Rotas para cada Cluster
    print("\n--- Análise de Rotas para cada Cluster ---")
    shortest_paths_info = {}
    
    for cluster_id in range(n_clusters):
        cluster_customers = df_customers[df_customers['cluster'] == cluster_id]
        
        # Encontra o ponto de entrega mais próximo do centróide
        centroid = kmeans.cluster_centers_[cluster_id]
        centroid_point = (centroid[0], centroid[1])
        
        # Encontra o cliente mais próximo do centroide como ponto de partida
        start_customer = cluster_customers.iloc[(cluster_customers[['latitude', 'longitude']] - centroid_point).pow(2).sum(axis=1).idxmin()]
        start_node_coords = (start_customer['latitude'], start_customer['longitude'])
        
        # Encontra o ponto de entrega mais distante como destino
        end_customer = cluster_customers.iloc[(cluster_customers[['latitude', 'longitude']] - start_node_coords).pow(2).sum(axis=1).idxmax()]
        end_node_coords = (end_customer['latitude'], end_customer['longitude'])
        
        # Encontrar o nó mais próximo no grafo para o ponto de partida e destino
        start_node = min(city_graph.nodes, key=lambda node: (city_graph.nodes[node]['pos'][0] - start_node_coords[0])**2 + (city_graph.nodes[node]['pos'][1] - start_node_coords[1])**2)
        end_node = min(city_graph.nodes, key=lambda node: (city_graph.nodes[node]['pos'][0] - end_node_coords[0])**2 + (city_graph.nodes[node]['pos'][1] - end_node_coords[1])**2)
        
        # Encontra a rota mais curta
        shortest_path, shortest_path_length = find_shortest_path(city_graph, start_node, end_node)
        
        if shortest_path:
            shortest_paths_info[cluster_id] = {
                'path': shortest_path,
                'length': shortest_path_length
            }
            print(f"Cluster {cluster_id}:")
            print(f"  Rota mais curta: {shortest_path}")
            print(f"  Distância total: {shortest_path_length:.2f} km")
        else:
            print(f"Cluster {cluster_id}: Não foi possível encontrar uma rota.")

    # --- Visualização Unificada: Grafo com Clusters e Rotas ---
    plt.figure(figsize=(12, 10))
    pos = nx.get_node_attributes(city_graph, 'pos')
    
    # Desenha o grafo da cidade
    nx.draw_networkx_nodes(city_graph, pos, node_color='lightblue', node_size=150, alpha=0.8)
    nx.draw_networkx_edges(city_graph, pos, edge_color='gray', style='--', alpha=0.6)
    nx.draw_networkx_labels(city_graph, pos)
    
    # Desenha os centróides dos clusters
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 1], centroids[:, 0], s=800, c='red', marker='X', label='Centróides', zorder=5, edgecolor='black', linewidth=1.5)
    
    # Define as cores para os clusters dos clientes
    cluster_colors = plt.cm.get_cmap('viridis', n_clusters)
    
    # Desenha os pontos de entrega (clientes)
    for cluster_id in range(n_clusters):
        cluster_customers = df_customers[df_customers['cluster'] == cluster_id]
        plt.scatter(cluster_customers['longitude'], cluster_customers['latitude'], 
                    s=250, c=[cluster_colors(cluster_id)], label=f'Cluster {cluster_id}', alpha=0.8, edgecolor='black', linewidth=0.5)

    # Desenha as rotas mais curtas
    for cluster_id, info in shortest_paths_info.items():
        path = info['path']
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(city_graph, pos, edgelist=path_edges, edge_color='red', width=3, label=f'Rota do Cluster {cluster_id}', style='-')
        
    plt.title('Grafo da Cidade, Clientes Agrupados e Rotas Otimizadas', fontsize=16)
    plt.xlabel('Longitude', fontsize=12)
    plt.ylabel('Latitude', fontsize=12)
    plt.legend(loc='best', fontsize=10)
    plt.grid(True)
    plt.show()

