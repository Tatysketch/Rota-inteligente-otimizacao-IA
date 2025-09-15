import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def perform_clustering():
    customer_data = {
        'id': [4, 5, 6, 8, 10, 11, 12, 13, 14],
        'latitude': [10, 25, 28, 5, 40, 42, 45, 8, 12],
        'longitude': [15, 30, 35, 20, 10, 12, 15, 25, 28]
    }
    df_customers = pd.DataFrame(customer_data)
    
    n_clusters = 2
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init=10)
    df_customers['cluster'] = kmeans.fit_predict(df_customers[['latitude', 'longitude']])
    
    print("--- Agrupamento de Clientes ---")
    print(df_customers)
    
    return df_customers, kmeans, n_clusters

def main_logic():
    df_customers, kmeans, n_clusters = perform_clustering()

    G = nx.Graph()
    for index, row in df_customers.iterrows():
        G.add_node(row['id'], pos=(row['longitude'], row['latitude']))
    
    pos_nodes = {node: G.nodes[node]['pos'] for node in G.nodes()}

    plt.figure(figsize=(10, 8))
    plt.scatter(df_customers['longitude'], df_customers['latitude'], c=df_customers['cluster'], s=200, cmap='viridis', alpha=0.7)
    plt.scatter(kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 0], s=500, c='red', marker='X', label='Centróides')
    
    plt.title('Pontos de Entrega Agrupados por K-Means', fontsize=16)
    plt.xlabel('Longitude', fontsize=12)
    plt.ylabel('Latitude', fontsize=12)
    plt.legend()
    plt.grid(True)

    for cluster_id in range(n_clusters):
        cluster_points = df_customers[df_customers['cluster'] == cluster_id]
        
        if len(cluster_points) > 1:
            subgraph_nodes = list(cluster_points['id'])
            edges_to_draw = [(subgraph_nodes[i], subgraph_nodes[i+1]) for i in range(len(subgraph_nodes)-1)]
            
            nx.draw_networkx_edges(G, pos=pos_nodes, edgelist=edges_to_draw, edge_color='red', width=2)
            
    plt.savefig('grafico_otimizacao.png')
    plt.show()

if __name__ == '__main__':
    main_logic()
