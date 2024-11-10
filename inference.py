from solvers.ckmeans import ck_get_clusters
from utils import create_subsets
from tqdm import tqdm
from models.gpt2 import score


words = input().split()
pairs = create_subsets(words, n=2)
scores = [[pair, score(pair, connector="and")] for pair in tqdm(pairs)]

adj = [[0.0 for i in range(16)] for i in range(16)]

for pair, result in scores:
    i = words.index(pair[0])
    j = words.index(pair[1])

    adj[i][j] = result
    adj[j][i] = result

labels = ck_get_clusters(adj)
clusters = [[] for i in range(4)]

for i, l in enumerate(labels):
    clusters[l].append(words[i])

clusters = sorted(clusters)

print(clusters)

if __name__ == '__main__':
    pass

