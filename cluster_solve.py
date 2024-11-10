from update_handler import load_connections
from solvers.kmeans import get_clusters
from solvers.ckmeans import ck_get_clusters
from solvers.ilp import get_clusters_ilp
from utils import create_subsets
from tqdm import tqdm
from models.qwen import score

data = load_connections()

idx = -1
puzzle = data[idx]

words, real = puzzle[0], puzzle[1]
pairs = create_subsets(words, n=2)
scores = [[pair, score(pair, connector="and")] for pair in tqdm(pairs)]

adj = [[0.0 for i in range(16)] for i in range(16)]

for pair, result in scores:
    i = words.index(pair[0])
    j = words.index(pair[1])

    adj[i][j] = result
    adj[j][i] = result

labels = ck_get_clusters(adj)
print(labels)
clusters = [[] for i in range(4)]
print(clusters)
for i, l in enumerate(labels):
    clusters[l].append(words[i])

clusters = sorted(clusters)

truth_clusters = sorted([x['words'] for x in real])

print(clusters)

print(truth_clusters)

if __name__ == '__main__':
    pass

