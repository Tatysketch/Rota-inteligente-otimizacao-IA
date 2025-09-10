import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from src.graph import create_graph, find_shortest_path
from src.clustering import perform_clustering

def main_logic():
    # Definição do dataset de cidades para o grafo
    cities = {
        'A': (30, 10), 'B': (20, 15), 'C': (25, 35), 'D': (10, 25), 
        'E': (40, 10), 'F': (45, 15), 'G': (42, 30), 'H': (5, 20),
        'I': (12, 28), 'J': (28, 5)
    }

    # 1. Agrupamento de Clientes
    # A função perform_clustering agora retorna dois valores, então ajustamos aqui
    df_customers, kmeans = perform_clustering()
    
    # 2. Cria o grafo da cidade
    # A função create_graph precisa receber o dicionário 'cities'
    city_graph = create_graph(cities)
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

        # O código original estava pegando o nome dos nós do grafo, mas os clientes são IDs
        # Mudei para pegar os IDs dos clientes diretamente
        print(f"--- Rota para o Entregador do Cluster {cluster_id} ---")
        print(" -> ".join(map(str, cluster_customers)))
        print(f"Tempo total de percurso: {total_time:.2f} minutos.\n")

if __name__ == '__main__':
    main_logic()


