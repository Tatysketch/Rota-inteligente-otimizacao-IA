import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def perform_clustering():
    """
    Realiza o agrupamento de clientes usando o algoritmo K-Means.
    """
    customer_data = {
        'id': [4, 5, 6, 8, 10, 11, 12, 13, 14],
        'latitude': [10, 25, 28, 5, 40, 42, 45, 8, 12],
        'longitude': [15, 30, 35, 20, 10, 12, 15, 25, 28]
    }
    df_customers = pd.DataFrame(customer_data)
    
    n_clusters = 3
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init=10)
    df_customers['cluster'] = kmeans.fit_predict(df_customers[['latitude', 'longitude']])
    
    print("--- Agrupamento de Clientes ---")
    print(df_customers)
    
    plt.figure(figsize=(10, 8))
    plt.scatter(df_customers['longitude'], df_customers['latitude'], c=df_customers['cluster'], s=200, cmap='viridis', alpha=0.7)
    plt.scatter(kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 0], s=500, c='red', marker='X', label='Centróides')
    plt.title('Pontos de Entrega Agrupados por K-Means', fontsize=16)
    plt.xlabel('Longitude', fontsize=12)
    plt.ylabel('Latitude', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

    return df_customers