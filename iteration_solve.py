from update_handler import load_connections
from solvers.kmeans import get_clusters
from solvers.ckmeans import ck_get_clusters
from solvers.ilp import get_clusters_ilp
from utils import create_subsets, min_swaps
from tqdm import tqdm
from models.qwen import score

data = load_connections()
slow = False


cur_tot = 0.0

for idx in range(len(data)):

    puzzle = data[idx]

    words, real = puzzle[0], puzzle[1]

    real = sorted([set(x['words']) for x in real])

    found = []

    while len(found) != 4:
        pairs = create_subsets(words, n=4)
        quad = sorted([[score(pair, connector="and", permute=slow), pair] for pair in tqdm(pairs)])[0][1]
        tmp = []
        for word in words:
            if word not in quad:
                tmp.append(word)

        words = tmp
        found.append(set(quad))
    real = sorted(real)
    found = sorted(found)
    print(found)
    print(real)

    distance = min_swaps(found, real)

    cur_tot += distance

    print("Current puzzle error:", distance)
    print("Average puzzle error:", cur_tot / (idx + 1))

if __name__ == '__main__':
    pass

