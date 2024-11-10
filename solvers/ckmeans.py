import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

def ck_get_clusters(X, n_clusters=4, cluster_size=4, max_iter=100):
    X = np.array(X)
    n_points = X.shape[0]
    assert n_clusters * cluster_size == n_points, "Total points must match clusters * cluster size"

    kmeans = KMeans(n_clusters=n_clusters, n_init=1, max_iter=1, random_state=0).fit(X)
    centroids = kmeans.cluster_centers_

    for iteration in range(max_iter):
        distances = cdist(X, centroids, 'euclidean')

        assigned_points = np.full(n_points, -1)
        cluster_counts = [0] * n_clusters

        for i in range(n_points):
            sorted_cluster_indices = np.argsort(distances[i])
            for cluster_idx in sorted_cluster_indices:
                if cluster_counts[cluster_idx] < cluster_size:
                    assigned_points[i] = cluster_idx
                    cluster_counts[cluster_idx] += 1
                    break

        if all(count == cluster_size for count in cluster_counts):
            break

        centroids = np.array([
            X[assigned_points == k].mean(axis=0) if np.sum(assigned_points == k) > 0 else centroids[k]
            for k in range(n_clusters)
        ])

    return assigned_points.tolist()
