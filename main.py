import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt 
from src.graph import create_graph, find_shortest_path
from src.clustering import perform_clustering
def main_logic():
    
    df_customers = perform_clustering()

    # 2. Cria o grafo da cidade
    city_graph = create_graph()
    hub_node = 0

    print("\n--- Otimização das Rotas por Entregador (Cluster) ---")
    
    n_clusters = df_customers['cluster'].nunique()
    
    for cluster_id in range(n_clusters):
        cluster_customers = df_customers[df_customers['cluster'] == cluster_id]['id'].tolist()
        
        # Encontra a rota do HUB para cada cliente no cluster
        current_node = hub_node
        total_route = []
        total_time = 0

        for customer_node in cluster_customers:
            path, time = find_shortest_path(city_graph, current_node, customer_node)
            if path:
                total_route.extend(path)
                total_time += time
                current_node = customer_node

        path_names = [city_graph.nodes[node]['name'] for node in total_route]
        
        print(f"--- Rota para o Entregador do Cluster {cluster_id} ---")
        print(" -> ".join(path_names))
        print(f"Tempo total de percurso: {total_time} minutos.\n")

if __name__ == '__main__':

    main_logic()

