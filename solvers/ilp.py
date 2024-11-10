import numpy as np
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

def get_clusters_ilp(adj):
    n_nodes = 16
    n_clusters = 4
    cluster_size = 4

    A = np.zeros((n_nodes, n_nodes))
    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            weight = adj[i][j]
            A[i, j] = weight
            A[j, i] = weight  # Symmetric for an undirected graph

    problem = LpProblem("BalancedClustering", LpMinimize)

    x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in range(n_clusters)] for i in range(n_nodes)]

    # d[i][j] = 1 if nodes i and j are in different clusters, 0 otherwise
    d = [[LpVariable(f"d_{i}_{j}", cat=LpBinary) for j in range(i + 1, n_nodes)] for i in range(n_nodes)]

    problem += lpSum(A[i][j] * d[i][j-i-1] for i in range(n_nodes) for j in range(i + 1, n_nodes))

    for i in range(n_nodes):
        problem += lpSum(x[i][j] for j in range(n_clusters)) == 1

    for j in range(n_clusters):
        problem += lpSum(x[i][j] for i in range(n_nodes)) == cluster_size

    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            for k in range(n_clusters):
                problem += d[i][j-i-1] >= x[i][k] - x[j][k]
                problem += d[i][j-i-1] >= x[j][k] - x[i][k]

    problem.solve()

    clusters = [[] for _ in range(n_clusters)]
    for i in range(n_nodes):
        for j in range(n_clusters):
            if x[i][j].varValue == 1:
                clusters[j].append(i)

    labels = [-1] * n_nodes
    for cluster_id, nodes in enumerate(clusters):
        for node in nodes:
            labels[node] = cluster_id

    return labels
