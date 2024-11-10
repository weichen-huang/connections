import numpy as np
from scipy.linalg import eigh
from sklearn.cluster import KMeans

np.random.seed(0)

def get_clusters(adj):

    A = np.zeros((16, 16))

    for i in range(16):
        for j in range(i + 1, 16):
            weight = adj[i][j]  # Replace with actual weight
            A[i, j] = weight
            A[j, i] = weight  # Symmetric for an undirected graph

    D = np.diag(A.sum(axis=1))

    D_inv_sqrt = np.diag(1.0 / np.sqrt(D.diagonal()))
    L_norm = np.eye(16) - D_inv_sqrt @ A @ D_inv_sqrt

    eigvals, eigvecs = eigh(L_norm)
    embedding = eigvecs[:, 1:4]  # Skip the first eigenvector

    kmeans = KMeans(n_clusters=4, random_state=0).fit(embedding)
    labels = kmeans.labels_

    return labels.tolist()